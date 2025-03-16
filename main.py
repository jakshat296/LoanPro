import sys
import locale
import logging
import socket
import requests
import random
import joblib
from retrying import retry
from PySide6.QtCore import QTimer
from datetime import datetime, timedelta
from interface import *
import mysql.connector
from PySide6 import QtCharts, QtWidgets, QtCore, QtGui
from PySide6.QtCharts import QChart, QChartView, QBarSeries, QBarSet, QValueAxis, QBarCategoryAxis
from PySide6.QtWidgets import QVBoxLayout, QMessageBox, QCompleter
from PySide6.QtCore import Qt, QStringListModel
from PySide6.QtGui import QStandardItemModel, QStandardItem
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

class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter
 

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
         QMainWindow.__init__(self)
         self.ui = Ui_MainWindow()
         self.ui.setupUi(self)
 
         self.ui.dashbtn.clicked.connect(lambda: self.on_dashbtn_clicked())
         self.ui.addbtn.clicked.connect(lambda: self.on_addbtn_clicked())
         self.ui.depositbtn.clicked.connect(lambda: self.on_depositbtn_clicked())
         self.ui.removebtn.clicked.connect(lambda: self.on_removebtn_clicked())
         self.ui.viewbtn_2.clicked.connect(lambda: self.update_active_tab(self.ui.viewbtn_2, 4))
         self.ui.accountsbtn.clicked.connect(lambda: self.update_active_tab(self.ui.accountsbtn, 5))
         self.ui.pushButton_15.clicked.connect(lambda: self.add_fingerprint())
         self.ui.pushButton_14.clicked.connect(lambda: self.add_record())
         self.ui.search_remove_2.clicked.connect(lambda: self.remove_record())
         self.ui.search_remove_3.clicked.connect(lambda: self.delete_record())
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
         self.completer_4 = QCompleter()
         self.completer_4.setCaseSensitivity(Qt.CaseInsensitive)
         self.completer_4.popup().setStyleSheet("font-size: 30px") 
         self.ui.remove_line_4.setCompleter(self.completer_4)
         self.ui.remove_line_4.textChanged.connect(self.update_completer_4_model)
         self.completer_5 = QCompleter()
         self.completer_5.setCaseSensitivity(Qt.CaseInsensitive)
         self.completer_5.popup().setStyleSheet("font-size: 30px") 
         self.ui.remove_line.setCompleter(self.completer_5)
         self.ui.remove_line.textChanged.connect(self.update_completer_5_model)
         self.ui.search_remove_4.clicked.connect(self.handle_deposit_search)
         self.ui.search_remove.clicked.connect(self.handle_remove_search)
         self.ui.search_remove_5.clicked.connect(self.handle_deposit)
         self.ui.tabWidget_2.currentChanged.connect(self.on_tab_changed)
         self.ui.tabWidget.currentChanged.connect(self.on_tab_changed_remove)
         self.ui.tableWidget_exist_6.setStyleSheet("QTableWidget {font-size: 30px;}")
         self.ui.tableWidget_exist_6.verticalHeader().setDefaultAlignment(Qt.AlignCenter)
         delegate = AlignDelegate(self.ui.tableWidget_exist_6)
         self.ui.tableWidget_exist_6.setItemDelegate(delegate)
         self.ui.tableWidget_exist_6.horizontalHeader().setDefaultSectionSize(170)
         self.ui.tableWidget_exist_5.setStyleSheet("QTableWidget {font-size: 30px;}")
         self.ui.tableWidget_exist_5.verticalHeader().setDefaultAlignment(Qt.AlignCenter)
         delegate = AlignDelegate(self.ui.tableWidget_exist_5)
         self.ui.tableWidget_exist_5.setItemDelegate(delegate)
         self.ui.tableWidget_exist_5.horizontalHeader().setDefaultSectionSize(170)
         delegate = AlignDelegate()
         self.ui.tableView_2.setItemDelegate(delegate)
         self.model = QStandardItemModel()
         self.model.setHorizontalHeaderLabels(["Date", "Amount"])
         self.ui.tableView_2.setModel(self.model)
         # Set the horizontal header properties
         header = self.ui.tableView_2.horizontalHeader()
         header.setSectionResizeMode(QHeaderView.Stretch)
         header.setStretchLastSection(True)
         # Set custom font for the horizontal header
         font = QFont()
         font.setPointSize(20)  # Set the font size to 14
         header.setFont(font)

         delegate = AlignDelegate()
         self.ui.tableView.setItemDelegate(delegate)
         self.model_2 = QStandardItemModel()
         self.model_2.setHorizontalHeaderLabels(["Date", "Amount"])
         self.ui.tableView.setModel(self.model_2)
         # Set the horizontal header properties
         header = self.ui.tableView.horizontalHeader()
         header.setSectionResizeMode(QHeaderView.Stretch)
         header.setStretchLastSection(True)
         # Set custom font for the horizontal header
         font = QFont()
         font.setPointSize(20)  # Set the font size to 14
         header.setFont(font)
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

    def on_removebtn_clicked(self):
        self.update_active_tab(self.ui.removebtn, 2)
        today_date = datetime.today().strftime('%Y-%m-%d')
        self.ui.remove_line_7.setText(today_date)
        self.ui.remove_line.clear()
        self.ui.remove_line_8.clear()
        self.ui.tableWidget_exist_5.setRowCount(0)
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.tabWidget.setCurrentIndex(0)
        self.model_2.clear()
        self.model_2.setHorizontalHeaderLabels(["Deposit Date", "Amount"])

    def on_depositbtn_clicked(self):
        self.update_active_tab(self.ui.depositbtn, 3)
        today_date = datetime.today().strftime('%Y-%m-%d')
        self.ui.remove_line_5.setText(today_date)
        self.ui.remove_line_4.clear()
        self.ui.remove_line_6.clear()
        self.ui.tableWidget_exist_6.setRowCount(0)
        self.ui.comboBox_2.setCurrentIndex(0)
        self.ui.tabWidget_2.setCurrentIndex(0)
        self.model.clear()
        self.model.setHorizontalHeaderLabels(["Deposit Date", "Amount"])
 
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
                        model = QStringListModel([str(i[0]) for i in result], self.completer_2)
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
                        model = QStringListModel([str(i[0]) for i in result], self.completer_3)
                        self.completer_3.setModel(model)
        except Exception as ex:
               QMessageBox.critical(self, "Error", f"{ex}")

    def update_completer_4_model(self):
        try:
                        connection = self.connect_to_database()
                        cursor = connection.cursor()
                        current = self.ui.comboBox_2.currentText()
                        text = self.ui.remove_line_4.text()
                        if current == "Name":
                                query = f'SELECT distinct(name) FROM all_records WHERE name LIKE "{text}%"'
                        elif current == "Location":
                                query = f'SELECT distinct(location) FROM all_records WHERE location LIKE "{text}%"'
                        elif current == "Fingerprint":
                                query = f'SELECT distinct(location) FROM all_records WHERE location LIKE "{text}%"'        
                        #execute and fetch data
                        cursor.execute(query)
                        result = cursor.fetchall()                        
                        # Update the completer's model
                        model = QStringListModel([str(i[0]) for i in result], self.completer_4)
                        self.completer_4.setModel(model)
        except Exception as ex:
               QMessageBox.critical(self, "Error", f"{ex}")


    def update_completer_5_model(self):
        try:
                        connection = self.connect_to_database()
                        cursor = connection.cursor()
                        current = self.ui.comboBox.currentText()
                        text = self.ui.remove_line.text()
                        if current == "Name":
                                query = f'SELECT distinct(name) FROM all_records WHERE name LIKE "{text}%"'
                        elif current == "Location":
                                query = f'SELECT distinct(location) FROM all_records WHERE location LIKE "{text}%"'
                        elif current == "Fingerprint":
                                query = f'SELECT distinct(location) FROM all_records WHERE location LIKE "{text}%"'        
                        #execute and fetch data
                        cursor.execute(query)
                        result = cursor.fetchall()                        
                        # Update the completer's model
                        model = QStringListModel([str(i[0]) for i in result], self.completer_5)
                        self.completer_5.setModel(model)
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

    def fingerprint_match(self, isoTemplateToMatch, fingerprint_data):
        try:
            connection = self.connect_to_database()
            cursor = connection.cursor()
            ipv4_address = get_ipv4_address()
            res2 = requests.post(f'https://{ipv4_address}:8003/mfs100/verify', data={
                "ProbTemplate": fingerprint_data,
                "GalleryTemplate": isoTemplateToMatch,
                "BioType": "FMR"
            }, verify=False)
            matchResponse = res2.json()
            if matchResponse.get('Status'):
                query = "select user_id from fingerprint_table where fingerprint_data = %s"
                cursor.execute(query, (fingerprint_data,))
                id = cursor.fetchone()
                return id[0]
        except Exception as e:
            QMessageBox.critical(None, "Error", str(e))
        return None

    def search_records(self, criteria, value):
        connection = self.connect_to_database()
        if connection:
            cursor = connection.cursor()
            try:
                query = ""
                if criteria == "Name":
                    query = "SELECT * FROM all_records WHERE Name LIKE %s"
                    cursor.execute(query, (f"%{value}%",))
                elif criteria == "Location":
                    query = "SELECT * FROM all_records WHERE Location LIKE %s"
                    cursor.execute(query, (f"%{value}%",))
                elif criteria == "Date":
                    query = "SELECT * FROM all_records WHERE DATE(date) = %s"
                    cursor.execute(query, (value,))
                elif criteria == "Fingerprint":
                    isoTemplateToMatch = capture_fingerprint()
                    print("akshat")
                    query = "SELECT fingerprint_data FROM fingerprint_table WHERE user_id IN (SELECT user_id FROM all_records WHERE Location LIKE %s)"
                    print("akshat")
                    cursor.execute(query, (f"%{value}%",))
                    print("akshat")
                    result = cursor.fetchall()
                    
                    ilist = []
                    
                    # Use joblib to parallelize fingerprint matching
                    num_jobs = 30
                    parallel = joblib.Parallel(n_jobs=num_jobs, backend="threading")  # Use threading backend for PyQt
                    fingerprint_matches = parallel(
                        joblib.delayed(self.fingerprint_match)(isoTemplateToMatch, i[0]) for i in result
                    )
                    # Collect the matching user IDs
                    ilist = [id for id in fingerprint_matches if id is not None]

                    if len(ilist) == 0:
                        QMessageBox.information(None, "No Match", f"No matching fingerprints found for customer in {value}")
                    else:
                        user_ids_str = ",".join(str(user_id) for user_id in ilist)
                        query = f"SELECT * FROM all_records WHERE user_id IN ({user_ids_str})"
                        cursor.execute(query)

                result = cursor.fetchall()
                return result
            except Exception as e:
                QMessageBox.critical(None, "Database Error", f"Error while searching records: {e}")
                return []
            finally:
                cursor.close()
                connection.close()
        else:
            QMessageBox.critical(None, "Database Error", "Failed to connect to the database.")
            return []

    def display_deposit_results(self,results):
        self.ui.tableWidget_exist_6.setRowCount(len(results))
        for row, record in enumerate(results):
            for column, item in enumerate(record):
                self.ui.tableWidget_exist_6.setItem(row, column, QTableWidgetItem(str(item)))


    # Handle search button click
    def handle_deposit_search(self):
        criteria = self.ui.comboBox_2.currentText()
        value = self.ui.remove_line_4.text().strip()
        results = self.search_records(criteria, value)
        self.display_deposit_results(results)

    def handle_remove_search(self):
        criteria = self.ui.comboBox.currentText()
        value = self.ui.remove_line.text().strip()
        results = self.search_records(criteria, value)
        self.display_remove_results(results)

    def display_remove_results(self,results):
        self.ui.tableWidget_exist_5.setRowCount(len(results))
        for row, record in enumerate(results):
            for column, item in enumerate(record):
                self.ui.tableWidget_exist_5.setItem(row, column, QTableWidgetItem(str(item)))
    
    # Get selected user_id from the table
    def get_selected_user_id(self):
        current_row = self.ui.tableWidget_exist_6.currentRow()
        if current_row != -1:
            return self.ui.tableWidget_exist_6.item(current_row, 0).text()
        return None
    
    # Get selected user_id from the table
    def get_selected_user_id_remove(self):
        current_row = self.ui.tableWidget_exist_5.currentRow()
        if current_row != -1:
            return self.ui.tableWidget_exist_5.item(current_row, 0).text()
        return None

    def add_deposit_to_database(self, user_id, deposit_amount):
        connection = self.connect_to_database()
        if connection:
            cursor = connection.cursor()
            try:
                # Insert the deposit into the deposits table
                deposit_date = self.ui.remove_line_5.text().strip()
                cursor.execute("INSERT INTO deposits (user_id, deposit_amount, deposit_date) VALUES (%s, %s, %s)", 
                            (user_id, deposit_amount, deposit_date))

                # Update the total deposit and last update in the all_records table
                query = f'''UPDATE all_records
                        SET deposit = IFNULL(deposit, 0) + {deposit_amount},
                        deposit_date = "{deposit_date}"
                        WHERE user_id = {user_id};'''
                cursor.execute(query)
                connection.commit()

                QMessageBox.information(None, "Success", "Deposit recorded successfully!")
                self.ui.remove_line_4.clear()
                self.ui.remove_line_6.clear()
                self.ui.tableWidget_exist_6.setRowCount(0)
                query = f"SELECT * FROM all_records WHERE user_id = {user_id}"
                cursor.execute(query)
                result = cursor.fetchall()
                self.display_deposit_results(result)
            except Exception as e:
                QMessageBox.critical(None, "Database Error", f"Error while updating deposit: {e}")
            finally:
                cursor.close()
                connection.close()
        else:
            QMessageBox.critical(None, "Database Error", "Failed to connect to the database.")

    # Handle deposit button click
    def handle_deposit(self):
        user_id = self.get_selected_user_id()
        deposit_amount = int(self.ui.remove_line_6.text().strip())
        if deposit_amount:
            self.add_deposit_to_database(user_id, deposit_amount)
            self.update_deposit_history(user_id)

    def get_deposit_history_from_database(self, user_id):
        connection = self.connect_to_database()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("SELECT deposit_date, deposit_amount FROM deposits WHERE user_id = %s ORDER BY deposit_date", 
                            (user_id,))
                result = cursor.fetchall()
                return result
            except Exception as e:
                QMessageBox.critical(None, "Database Error", f"Error while fetching deposit history: {e}")
                return []
            finally:
                cursor.close()
                connection.close()
        else:
            QMessageBox.critical(None, "Database Error", "Failed to connect to the database.")
            return []

    def display_deposit_history(self, user_id):
        deposit_history = self.get_deposit_history_from_database(user_id)
        self.model.clear()
        self.model.setHorizontalHeaderLabels(["Deposit_Date", "Amount"])
        for row, item in enumerate(deposit_history):
            date_item = QStandardItem(item[0].strftime("%Y-%m-%d"))
            amount_item = QStandardItem(str(item[1]))
            self.model.appendRow([date_item, amount_item])

    def display_deposit_history_remove(self, user_id):
        deposit_history = self.get_deposit_history_from_database(user_id)
        self.model_2.clear()
        self.model_2.setHorizontalHeaderLabels(["Deposit_Date", "Amount"])
        for row, item in enumerate(deposit_history):
            date_item = QStandardItem(item[0].strftime("%Y-%m-%d"))
            amount_item = QStandardItem(str(item[1]))
            self.model_2.appendRow([date_item, amount_item])

    # Update deposit history in the table view
    def update_deposit_history(self, user_id):
        deposit_history = self.get_deposit_history_from_database(user_id)
        self.model.clear()
        self.model.setHorizontalHeaderLabels(["Deposit_Date", "Amount"])
        for row, item in enumerate(deposit_history):
            date_item = QStandardItem(item[0].strftime("%Y-%m-%d"))
            amount_item = QStandardItem(str(item[1]))
            self.model.appendRow([date_item, amount_item])

    # Update deposit history in the table view
    def update_deposit_history_remove(self, user_id):
        deposit_history = self.get_deposit_history_from_database(user_id)
        self.model_2.clear()
        self.model_2.setHorizontalHeaderLabels(["Deposit_Date", "Amount"])
        for row, item in enumerate(deposit_history):
            date_item = QStandardItem(item[0].strftime("%Y-%m-%d"))
            amount_item = QStandardItem(str(item[1]))
            self.model_2.appendRow([date_item, amount_item])

    # Handle tab change event
    def on_tab_changed(self, index):
        if index == 1:  # Deposit history tab
            user_id = self.get_selected_user_id()
            if user_id:
                self.update_deposit_history(user_id)
    
    # Handle tab change event
    def on_tab_changed_remove(self, index):
        if index == 1:  # Deposit history tab
            user_id = self.get_selected_user_id_remove()
            if user_id:
                self.update_deposit_history_remove(user_id)

    def remove_record(self):
        # Check if interest is provided
        if not self.ui.remove_line_8.text().strip():
            QMessageBox.critical(None, "Error", "Interest is required")
            return

        interest = self.ui.remove_line_8.text().strip()
        user_id = self.get_selected_user_id_remove()

        if not user_id:
            QMessageBox.critical(None, "Error", "User ID is required")
            return
        
        try:
            current_date = datetime.today().strftime('%Y-%m-%d')
            deposit_amt = self.get_deposit_amount(user_id)
            date_edit = self.ui.remove_line_7.text().strip()

            if deposit_amt is not None:
                self.update_daily_assessment(deposit_amt, current_date)

            self.insert_into_removed_records(user_id)
            self.delete_from_fingerprint_table(user_id)
            self.delete_from_all_records(user_id)
            self.update_removed_records_interest(user_id, interest)
            self.update_removed_records_date(user_id, date_edit)
            QMessageBox.information(None, "Success", "Record removed successfully")
            self.handle_remove_search()
        except Exception as e:
            QMessageBox.critical(None, "Database Error", str(e))

    def delete_record(self):
        try:
            user_id = self.get_selected_user_id_remove()
            self.delete_from_fingerprint_table(user_id)
            self.delete_from_all_records(user_id)
            QMessageBox.information(None, "Success", "Record deleted successfully")
            self.on_removebtn_clicked()
        except Exception as e:
            QMessageBox.critical(None, "Database Error", str(e))


    def get_deposit_amount(self, user_id):
        connection = self.connect_to_database()
        cursor = connection.cursor()
        query = 'SELECT deposit FROM all_records WHERE user_id = %s'
        cursor.execute(query, (user_id,))
        deposit_amt = cursor.fetchone()
        return int(deposit_amt[0]) if deposit_amt and deposit_amt[0] is not None else None

    def update_daily_assessment(self, deposit_amt, current_date):
        connection = self.connect_to_database()
        cursor = connection.cursor()
        query = '''UPDATE daily_assessment
                   SET deposit_debit = COALESCE(deposit_debit, 0) + %s
                   WHERE date = %s;'''
        values = (deposit_amt, current_date)
        cursor.execute(query, values)
        connection.commit()

    def insert_into_removed_records(self, user_id):
        connection = self.connect_to_database()
        cursor = connection.cursor()
        query = f'''INSERT INTO removed_records (user_id, amount, name, father_name, location, Date, Type, Weight) 
                   SELECT user_id, amount, name, father_name, location, Date, Type, Weight 
                   FROM all_records 
                   WHERE user_id = %s;'''
        cursor.execute(query, (user_id,))
        connection.commit()

    def delete_from_fingerprint_table(self, user_id):
        connection = self.connect_to_database()
        cursor = connection.cursor()
        query = 'DELETE FROM fingerprint_table WHERE user_id = %s;'
        cursor.execute(query, (user_id,))
        connection.commit()
        print("akshat")

    def delete_from_all_records(self, user_id):
        connection = self.connect_to_database()
        cursor = connection.cursor()
        query = 'DELETE FROM all_records WHERE user_id = %s;'
        cursor.execute(query, (user_id,))
        connection.commit()

    def update_removed_records_interest(self, user_id, interest):
        connection = self.connect_to_database()
        cursor = connection.cursor()
        query = 'UPDATE removed_records SET interest = %s WHERE user_id = %s'
        values = (interest, user_id)
        cursor.execute(query, values)
        connection.commit()

    def update_removed_records_date(self, user_id, date_edit):
        connection = self.connect_to_database()
        cursor = connection.cursor()
        query = 'UPDATE removed_records SET removed_date = %s WHERE user_id = %s'
        values = (date_edit, user_id)
        cursor.execute(query, values)
        connection.commit()


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
