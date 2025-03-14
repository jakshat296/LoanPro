import sys
import locale
import logging
import socket
import requests
import random
from retrying import retry
from PySide6.QtCore import QTimer
from datetime import datetime, timedelta
from interface import *
import mysql.connector
from PySide6 import QtCharts
from PySide6.QtCharts import QChart, QChartView, QBarSeries, QBarSet, QValueAxis, QBarCategoryAxis
from PySide6.QtWidgets import QVBoxLayout, QMessageBox, QCompleter
from PySide6.QtCore import Qt, QStringListModel
from decimal import Decimal
from Custom_Widgets.Widgets import *  # Import the loadJsonStyle function



# Configure logging
logging.basicConfig(filename='fingerprint_capture.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_ipv4_address():
    try:
        # Create a socket to get the local machine's hostname
        hostname = socket.gethostname()

        # Get the IPv4 address corresponding to the hostname
        ipv4_address = socket.gethostbyname(hostname)

        return ipv4_address
    except socket.error as e:
        logging.error("Failed to get IPv4 address: %s", e)
        return None

@retry(stop_max_attempt_number=3, wait_fixed=2000)
def capture_fingerprint():
    ipv4_address = get_ipv4_address()
    if not ipv4_address:
        raise Exception("Failed to get IPv4 address")

    url = f'https://{ipv4_address}:8003/mfs100/capture'
    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }
    data = {
        "Quality": 60,
        "TimeOut": 10
    }
    
    try:
        logging.info("Sending capture request to %s", url)
        res = requests.post(url, json=data, headers=headers, verify=False)
        res.raise_for_status()
        response_data = res.json()

        if response_data.get("ErrorCode") == "0":
            isoTemplate = response_data['IsoTemplate']
            logging.info("Fingerprint captured successfully")
            return isoTemplate
        else:
            error_description = response_data.get("ErrorDescription", "Unknown error")
            logging.error("Capture failed: %s", error_description)
            raise Exception(f"Capture failed: {error_description}")
    except requests.exceptions.RequestException as e:
        logging.error("Capture attempt failed. Error: %s", e)
        raise
    except KeyError as e:
        logging.error("Unexpected response format: %s", e)
        raise
 

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
         QMainWindow.__init__(self)
         self.ui = Ui_MainWindow()
         self.ui.setupUi(self)
 
         self.ui.dashbtn.clicked.connect(lambda: self.on_dashbtn_clicked())
         self.ui.addbtn.clicked.connect(lambda: self.on_addbtn_clicked())
         self.ui.removebtn.clicked.connect(lambda: self.update_active_tab(self.ui.removebtn, 2))
         self.ui.depositbtn.clicked.connect(lambda: self.update_active_tab(self.ui.depositbtn, 3))
         self.ui.viewbtn_2.clicked.connect(lambda: self.update_active_tab(self.ui.viewbtn_2, 4))
         self.ui.accountsbtn.clicked.connect(lambda: self.update_active_tab(self.ui.accountsbtn, 5))
         self.ui.pushButton_15.clicked.connect(lambda: self.add_fingerprint())
         self.ui.pushButton_14.clicked.connect(lambda: self.add_record())
         self.completer_1 = QCompleter()
         self.completer_1.setCaseSensitivity(Qt.CaseInsensitive)
         self.completer_1.popup().setStyleSheet("font-size: 30px") 
         self.ui.location_line.setCompleter(self.completer_1)
         self.ui.location_line.textChanged.connect(self.update_completer_1_model)
         self.completer_2 = QCompleter()
         self.completer_2.setCaseSensitivity(Qt.CaseInsensitive)
         self.completer_2.popup().setStyleSheet("font-size: 30px") 
         self.ui.name_line.setCompleter(self.completer_2)
         self.ui.name_line.textChanged.connect(self.update_completer_2_model)
         self.completer_3 = QCompleter()
         self.completer_3.setCaseSensitivity(Qt.CaseInsensitive)
         self.completer_3.popup().setStyleSheet("font-size: 30px") 
         self.ui.father_line.setCompleter(self.completer_3)
         self.ui.father_line.textChanged.connect(self.update_completer_3_model)

         loadJsonStyle(self, self.ui)
         self.update_active_tab(self.ui.dashbtn, 0)
         self.update_labels()
         self.update_charts()
         self.show()

    def on_dashbtn_clicked(self):
        self.update_active_tab(self.ui.dashbtn, 0)
        self.update_labels()
        self.update_charts()

    def on_addbtn_clicked(self):
        self.update_active_tab(self.ui.addbtn, 1)
        today_date = datetime.today().strftime('%Y-%m-%d')
        self.ui.date_line.setText(today_date)
 
    def update_active_tab(self, active_button, page_index):
        buttons = [self.ui.dashbtn, self.ui.addbtn, self.ui.removebtn, self.ui.depositbtn, self.ui.viewbtn_2, self.ui.accountsbtn]
        icons_inactive = {
             self.ui.dashbtn: ":/white icons/assets/icons/white/bar-chart.svg",
             self.ui.addbtn: ":/white icons/assets/icons/white/plus.svg",
             self.ui.removebtn: ":/white icons/assets/icons/white/x.svg",
             self.ui.depositbtn: ":/white icons/assets/icons/white/folder-plus.svg",
             self.ui.viewbtn_2: ":/white icons/assets/icons/white/check-square.svg",
             self.ui.accountsbtn: ":/white icons/assets/icons/white/book-open.svg"
         }
        icons_active = {
             self.ui.dashbtn: ":/whiteicons/assets/icons/blue/bar-chart.svg",
             self.ui.addbtn: ":/whiteicons/assets/icons/blue/plus.svg",
             self.ui.removebtn: ":/whiteicons/assets/icons/blue/x.svg",
             self.ui.depositbtn: ":/whiteicons/assets/icons/blue/folder-plus.svg",
             self.ui.viewbtn_2: ":/whiteicons/assets/icons/blue/check-square.svg",
             self.ui.accountsbtn: ":/whiteicons/assets/icons/blue/book-open.svg"
        }

        header_texts = {
            self.ui.dashbtn: "Dashboard",
            self.ui.addbtn: "Add New Record",
            self.ui.removebtn: "Remove Record",
            self.ui.depositbtn: "Add Deposit",
            self.ui.viewbtn_2: "View Records",
            self.ui.accountsbtn: "Accounts"
        }
 
        for button in buttons:
            if button == active_button:
                button.setStyleSheet("""
                     background-color: #fefeff;
                     padding: 10px 5px;
                     text-align: left;
                     border-top-left-radius: 20px;
                     color: #2596be;
                 """)
                self.ui.appheader_4.setText(header_texts[button])
                button.setIcon(QIcon(icons_active[button]))
 
            else:
                button.setStyleSheet("""
                     background-color: #2596be;
                     padding: 10px 5px;
                     text-align: left;
                     border-top-left-radius: 20px;
                     color: #fff;
                     border: none;
                 """)
                button.setIcon(QIcon(icons_inactive[button]))
 
        # Change the page in the stacked widget
        self.ui.stackedWidget.setCurrentIndex(page_index)

    def connect_to_database(self):
        """Connect to the MySQL database and return the connection object."""
        connection = mysql.connector.connect(
            host='localhost',
            database='loan_management',
            user='root',
            password='akshat'
        )
        if connection.is_connected():
            return connection
        
    def update_labels(self):
        """Update the labels with the sum of amount and count of entries from the all_records table."""
        connection = self.connect_to_database()
        if connection:
            cursor = connection.cursor()
            # Calculate the sum of amount
            cursor.execute("SELECT SUM(amount) FROM all_records")
            sum_amount = cursor.fetchone()[0]
            sum_amount = sum_amount if sum_amount else 0

            # Set locale to Indian format
            locale.setlocale(locale.LC_ALL, 'en_IN')
            formatted_amount = locale.format_string("%d", sum_amount, grouping=True)
            formatted_amount = f"₹ {formatted_amount}"
            self.ui.label_56.setText(f"{formatted_amount}")

            # Count the number of entries
            cursor.execute("SELECT COUNT(*) FROM all_records")
            count_entries = cursor.fetchone()[0]
            self.ui.label_57.setText(f"[{count_entries}]")

            # Get today's date
            today_date = datetime.today().strftime('%Y-%m-%d')

            # Calculate the sum of amount for today
            cursor.execute("SELECT SUM(amount) FROM all_records WHERE DATE(date) = %s", (today_date,))
            sum_amount_today = cursor.fetchone()[0]
            sum_amount_today = sum_amount_today if sum_amount_today else 0

            # Set locale to Indian format and add Indian currency symbol for today's amount
            formatted_amount_today = locale.format_string("%d", sum_amount_today, grouping=True)
            formatted_amount_today = f"₹ {formatted_amount_today}"

            self.ui.label_60.setText(f"{formatted_amount_today}")

            # Count the number of entries for today
            cursor.execute("SELECT COUNT(*) FROM all_records WHERE DATE(date) = %s", (today_date,))
            count_entries_today = cursor.fetchone()[0]
            self.ui.label_61.setText(f"[{count_entries_today}]")

            # Calculate the sum of amount for today from removed_records
            cursor.execute("SELECT SUM(amount+interest) FROM removed_records WHERE removed_date = %s", (today_date,))
            sum_amount_returns_today = cursor.fetchone()[0]
            sum_amount_returns_today = sum_amount_returns_today if sum_amount_returns_today else 0

            # Set locale to Indian format and add Indian currency symbol for today's returns amount
            formatted_amount_returns_today = locale.format_string("%d", sum_amount_returns_today, grouping=True)
            formatted_amount_returns_today = f"₹ {formatted_amount_returns_today}"

            self.ui.label_64.setText(f"{formatted_amount_returns_today}")

            # Count the number of entries for today from removed_records
            cursor.execute("SELECT COUNT(*) FROM removed_records WHERE removed_date = %s", (today_date,))
            count_entries_returns_today = cursor.fetchone()[0]
            self.ui.label_65.setText(f"[{count_entries_returns_today}]")

            # Calculate today's interest from the interest column in removed_records
            cursor.execute("SELECT SUM(interest) FROM removed_records WHERE removed_date = %s", (today_date,))
            sum_interest_today = cursor.fetchone()[0]
            sum_interest_today = sum_interest_today if sum_interest_today else 0

            # Set locale to Indian format and add Indian currency symbol for today's interest
            formatted_interest_today = locale.format_string("%d", sum_interest_today, grouping=True)
            formatted_interest_today = f"₹ {formatted_interest_today}"

            self.ui.label_68.setText(f"{formatted_interest_today}")

            cursor.close()
            connection.close()
    
    
    def update_charts(self):
        """Update the bar charts for the last 5 days statistics of investment, returns, and interest."""
        try:
            def create_chart(data, title):
                """Helper function to create a bar chart."""
                series = QBarSeries()
                bar_set = QBarSet(title)
                bar_set.append(data)
                series.append(bar_set)

                chart = QChart()
                chart.addSeries(series)
                chart.setTitle(title)
                chart.setAnimationOptions(QChart.SeriesAnimations)

                categories = []
                for i in range(5):
                    categories.append((datetime.today() - timedelta(days=i)).strftime('%d-%m-%Y'))

                axisX = QBarCategoryAxis()
                axisX.append(categories)
                chart.addAxis(axisX, Qt.AlignBottom)
                series.attachAxis(axisX)

                axisY = QValueAxis()
                axisY.setRange(0, float(max(data)) * 1.1)  # Convert to float
                chart.addAxis(axisY, Qt.AlignLeft)
                series.attachAxis(axisY)

                chart.legend().hide()

                return chart

            def fetch_data_for_last_5_days(query):
                """Helper function to fetch data for the last 5 days from the database."""
                connection = self.connect_to_database()
                if connection:
                    cursor = connection.cursor()
                    cursor.execute(query)
                    data = [float(row[1]) for row in cursor.fetchall()]  # Convert to float
                    cursor.close()
                    connection.close()
                    return data
                else:
                    return [0, 0, 0, 0, 0]

            current_date = datetime.today().strftime('%Y-%m-%d')
            investment_query = f"""
                SELECT
                    DATE(calendar.date) AS date,
                    IFNULL(SUM(all_records.amount), 0) AS total_investment
                FROM
                    (
                        SELECT "{current_date}" AS date
                        UNION ALL
                        SELECT DATE_SUB("{current_date}", INTERVAL 1 DAY)
                        UNION ALL
                        SELECT DATE_SUB("{current_date}", INTERVAL 2 DAY)
                        UNION ALL
                        SELECT DATE_SUB("{current_date}", INTERVAL 3 DAY)
                        UNION ALL
                        SELECT DATE_SUB("{current_date}", INTERVAL 4 DAY)
                    ) AS calendar
                LEFT JOIN
                    all_records ON calendar.date = DATE(all_records.date)
                GROUP BY
                    calendar.date
                ORDER BY
                    calendar.date DESC;
            """

            returns_query = f"""
                SELECT
                    DATE(calendar.date) AS date,
                    IFNULL(SUM(removed_records.amount), 0) AS total_returns
                FROM
                    (
                        SELECT "{current_date}" AS date
                        UNION ALL
                        SELECT DATE_SUB("{current_date}", INTERVAL 1 DAY)
                        UNION ALL
                        SELECT DATE_SUB("{current_date}", INTERVAL 2 DAY)
                        UNION ALL
                        SELECT DATE_SUB("{current_date}", INTERVAL 3 DAY)
                        UNION ALL
                        SELECT DATE_SUB("{current_date}", INTERVAL 4 DAY)
                    ) AS calendar
                LEFT JOIN
                    removed_records ON calendar.date = DATE(removed_records.removed_date)
                GROUP BY
                    calendar.date
                ORDER BY
                    calendar.date DESC;
            """

            interest_query = f"""
                SELECT
                    DATE(calendar.date) AS date,
                    IFNULL(SUM(removed_records.interest), 0) AS total_interest
                FROM
                    (
                        SELECT "{current_date}" AS date
                        UNION ALL
                        SELECT DATE_SUB("{current_date}", INTERVAL 1 DAY)
                        UNION ALL
                        SELECT DATE_SUB("{current_date}", INTERVAL 2 DAY)
                        UNION ALL
                        SELECT DATE_SUB("{current_date}", INTERVAL 3 DAY)
                        UNION ALL
                        SELECT DATE_SUB("{current_date}", INTERVAL 4 DAY)
                    ) AS calendar
                LEFT JOIN
                    removed_records ON calendar.date = DATE(removed_records.removed_date)
                GROUP BY
                    calendar.date
                ORDER BY
                    calendar.date DESC;
            """

            investment_data = fetch_data_for_last_5_days(investment_query)
            returns_data = fetch_data_for_last_5_days(returns_query)
            interest_data = fetch_data_for_last_5_days(interest_query)

            investment_chart = create_chart(investment_data, "Total Investment")
            returns_chart = create_chart(returns_data, "Total Returns")
            interest_chart = create_chart(interest_data, "Total Interest")

            self.ui.graphicsView_2.setChart(investment_chart)
            self.ui.graphicsView_3.setChart(returns_chart)
            self.ui.graphicsView.setChart(interest_chart)

            self.ui.invesbtn_4.clicked.connect(lambda: self.ui.stackedWidget_5.setCurrentIndex(0))
            self.ui.invesbtn_4.clicked.connect(lambda: self.ui.graphicsView_2.setChart(investment_chart))
            self.ui.returnbtn_4.clicked.connect(lambda: self.ui.stackedWidget_5.setCurrentIndex(1))
            self.ui.returnbtn_4.clicked.connect(lambda: self.ui.graphicsView_3.setChart(returns_chart))
            self.ui.interestbtn_4.clicked.connect(lambda: self.ui.stackedWidget_5.setCurrentIndex(2))
            self.ui.interestbtn_4.clicked.connect(lambda: self.ui.graphicsView.setChart(interest_chart))

        except Exception as e:
            print(f"An error occurred in update_charts: {e}")
            self.show_message_box("Error", f"An error occurred while updating charts: {e}")

    
    def update_completer_1_model(self):
        try:
                        connection = self.connect_to_database()
                        cursor = connection.cursor()
                        text = self.ui.location_line.text()
                        query = f'SELECT distinct(location) FROM all_records WHERE location LIKE "{text}%"'
                        #execute and fetch data
                        cursor.execute(query)
                        result = cursor.fetchall()                        
                        # Update the completer's model
                        model = QStringListModel([str(i[0]) for i in result], self.completer_1)
                        self.completer_1.setModel(model)
        except Exception as ex:
               QMessageBox.critical(self, "Error", f"{ex}")

    def update_completer_2_model(self):
        try:
                        connection = self.connect_to_database()
                        cursor = connection.cursor()
                        text = self.ui.name_line.text()
                        query = f'SELECT distinct(name) FROM all_records WHERE Name LIKE "{text}%"'
                        #execute and fetch data
                        cursor.execute(query)
                        result = cursor.fetchall()                        
                        # Update the completer's model
                        model = QStringListModel([str(i[0]) for i in result], self.completer_1)
                        self.completer_2.setModel(model)
        except Exception as ex:
               QMessageBox.critical(self, "Error", f"{ex}")

    def update_completer_3_model(self):
        try:
                        connection = self.connect_to_database()
                        cursor = connection.cursor()
                        text = self.ui.father_line.text()
                        query = f'SELECT distinct(father_name) FROM all_records WHERE father_name LIKE "{text}%"'
                        #execute and fetch data
                        cursor.execute(query)
                        result = cursor.fetchall()                        
                        # Update the completer's model
                        model = QStringListModel([str(i[0]) for i in result], self.completer_1)
                        self.completer_3.setModel(model)
        except Exception as ex:
               QMessageBox.critical(self, "Error", f"{ex}")

    def generate_unique_user_id(self):
        connection = self.connect_to_database()
        cursor = connection.cursor()

        while True:
            user_id = random.randint(1, 10000)  # Generate a random user_id
            cursor.execute("SELECT COUNT(*) FROM all_records WHERE User_id = %s", (user_id,))
            if cursor.fetchone()[0] == 0:
                break

        cursor.close()
        connection.close()
        return user_id
    
    def collect_user_data(self):
        name = self.ui.name_line.text().strip()
        father_name = self.ui.father_line.text().strip()
        location = self.ui.location_line.text().strip()
        amount = self.ui.amount_line.text().strip()
        date = self.ui.date_line.text().strip()
        type_ = self.ui.jewellery_line.text().strip()
        weight = self.ui.weight_line.text().strip()

        if not name or not father_name or not location or not amount or not weight:
            QMessageBox.critical(self, "Error", "Please fill in all required fields.")
            return None
        else:
            return {
                "name": name[0].upper() + name[1:].lower(),
                "father_name": father_name[0].upper() + father_name[1:].lower(),
                "location": location[0].upper() + location[1:].lower(),
                "amount": int(amount),
                "date": date,
                "type": type_[0].upper() + type_[1:].lower(),
                "weight": int(weight)
            }


    def add_record_to_all_records(self, user_data, user_id):
        connection = self.connect_to_database()
        cursor = connection.cursor()
        query = """
        INSERT INTO all_records (User_id, Amount, Name, Father_name, Location, Date, type, weight)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            user_id,
            user_data["amount"],
            user_data["name"],
            user_data["father_name"],
            user_data["location"],
            user_data["date"],
            user_data["type"],
            user_data["weight"]
        ))
        connection.commit()
        cursor.close()
        connection.close()
    
    def add_fingerprint_to_fingerprint_table(self, user_id, fingerprint_data):
        connection = self.connect_to_database()
        cursor = connection.cursor()
        query = """
        INSERT INTO fingerprint_table (user_id, fingerprint_data)
        VALUES (%s, %s)
        """
        cursor.execute(query, (user_id, fingerprint_data))
        connection.commit()
        cursor.close()
        connection.close()

    def add_record(self):
        self.ui.pushButton_14.setEnabled(False)
        try:
            global user_id
            user_data = self.collect_user_data()
            user_id = self.generate_unique_user_id()
            self.add_record_to_all_records(user_data, user_id)
            QMessageBox.information(self, "Success", "Record added successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        finally:
            QTimer.singleShot(6000, lambda: self.ui.pushButton_14.setEnabled(True))  # Re-enable the button after 6 seconds

    def add_fingerprint(self):
        self.ui.pushButton_15.setEnabled(False)
        try:
            fingerprint_data = capture_fingerprint()
            self.add_fingerprint_to_fingerprint_table(user_id, fingerprint_data)
            QMessageBox.information(self, "Success", "Fingerprint added successfully!")
            self.clear()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        finally:
            QTimer.singleShot(6000, lambda: self.ui.pushButton_15.setEnabled(True))


    def clear(self):
        self.ui.name_line.clear()
        self.ui.father_line.clear()
        self.ui.amount_line.clear()
        self.ui.location_line.clear()
        self.ui.jewellery_line.clear()
        self.ui.weight_line.clear()
    

    def show_message_box(self, title, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

if __name__ == "__main__":
     app = QApplication(sys.argv)
     window = MainWindow()
     window.show()
     sys.exit(app.exec())
