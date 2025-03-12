import sys
import locale
from interface import *
from Custom_Widgets.Widgets import *  # Import the loadJsonStyle function
import mysql.connector
from datetime import datetime, timedelta
from PyQt5.QtChart import QChart, QChartView, QBarSeries, QBarSet, QValueAxis, QBarCategoryAxis
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QApplication, QMainWindow
from mysql.connector import Error


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        try:
            super(MainWindow, self).__init__(parent)
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)

            self.ui.dashbtn.clicked.connect(lambda: self.update_active_tab(self.ui.dashbtn, 0))
            self.ui.addbtn.clicked.connect(lambda: self.update_active_tab(self.ui.addbtn, 1))
            self.ui.removebtn.clicked.connect(lambda: self.update_active_tab(self.ui.removebtn, 2))
            self.ui.depositbtn.clicked.connect(lambda: self.update_active_tab(self.ui.depositbtn, 3))
            self.ui.viewbtn_2.clicked.connect(lambda: self.update_active_tab(self.ui.viewbtn_2, 4))
            self.ui.accountsbtn.clicked.connect(lambda: self.update_active_tab(self.ui.accountsbtn, 5))
            loadJsonStyle(self, self.ui)
            self.update_active_tab(self.ui.dashbtn, 0)
            self.show()
            self.update_labels()
            self.update_charts()
        except Exception as e:
            print(f"An error occurred during initialization: {e}")
            sys.exit(1)

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
            self.ui.depositbtn: "Deposit Funds",
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
                button.setIcon(QIcon(icons_active[button]))
                self.ui.appheader_4.setText(header_texts[button])
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
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='loan_management',
                user='root',
                password='akshat'
            )
            if connection.is_connected():
                return connection
        except Error as e:
            self.show_message_box("Database Connection Error", f"Error while connecting to MySQL: {e}")
            return None

    def update_labels(self):
        """Update the labels with the sum of amount and count of entries from the all_records table."""
        try:
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
                cursor.execute("SELECT SUM(amount) FROM removed_records WHERE removed_date = %s", (today_date,))
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
        except Exception as e:
            print(f"An error occurred in update_labels: {e}")
            self.show_message_box("Error", f"An error occurred while updating labels: {e}")

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

                categories = [datetime.today().strftime('%Y-%m-%d')]
                for i in range(1, 5):
                    categories.insert(0, (datetime.today() - timedelta(days=i)).strftime('%Y-%m-%d'))

                axisX = QBarCategoryAxis()
                axisX.append(categories)
                chart.addAxis(axisX, Qt.AlignBottom)
                series.attachAxis(axisX)

                axisY = QValueAxis()
                axisY.setRange(0, max(data) * 1.1)
                chart.addAxis(axisY, Qt.AlignLeft)
                series.attachAxis(axisY)

                return chart

            def fetch_data_for_last_5_days(query):
                """Helper function to fetch data for the last 5 days from the database."""
                connection = self.connect_to_database()
                if connection:
                    cursor = connection.cursor()
                    data = []
                    for i in range(5):
                        date = (datetime.today() - timedelta(days=i)).strftime('%Y-%m-%d')
                        cursor.execute(query, (date,))
                        result = cursor.fetchone()[0]
                        data.insert(0, result if result else 0)
                    cursor.close()
                    connection.close()
                    return data
                else:
                    return [0, 0, 0, 0, 0]

            # Queries to fetch data for the last 5 days
            investment_query = "SELECT SUM(amount) FROM all_records WHERE DATE(date) = %s"
            returns_query = "SELECT SUM(amount) FROM removed_records WHERE DATE(date) = %s"
            interest_query = "SELECT SUM(interest) FROM removed_records WHERE DATE(date) = %s"

            # Fetch data from the database
            investment_data = fetch_data_for_last_5_days(investment_query)
            returns_data = fetch_data_for_last_5_days(returns_query)
            interest_data = fetch_data_for_last_5_days(interest_query)

            # Create charts
            investment_chart = create_chart(investment_data, "Last 5 Days Investment")
            returns_chart = create_chart(returns_data, "Last 5 Days Returns")
            interest_chart = create_chart(interest_data, "Last 5 Days Interest")

            # Create QChartViews for the charts
            investment_chart_view = QChartView(investment_chart)
            returns_chart_view = QChartView(returns_chart)
            interest_chart_view = QChartView(interest_chart)

            # Ensure layouts are set for the widgets
            if self.ui.Ichart_4.layout() is None:
                self.ui.Ichart_4.setLayout(QVBoxLayout())
            if self.ui.Rchart_4.layout() is None:
                self.ui.Rchart_4.setLayout(QVBoxLayout())
            if self.ui.Inchart_4.layout() is None:
                self.ui.Inchart_4.setLayout(QVBoxLayout())

            # Clear existing layouts to avoid multiple charts
            self.clear_layout(self.ui.Ichart_4.layout())
            self.clear_layout(self.ui.Rchart_4.layout())
            self.clear_layout(self.ui.Inchart_4.layout())

            # Set charts to respective widgets
            self.ui.Ichart_4.layout().addWidget(investment_chart_view)
            self.ui.Rchart_4.layout().addWidget(returns_chart_view)
            self.ui.Inchart_4.layout().addWidget(interest_chart_view)

            # Set up button click events to change stacked widget index
            self.ui.invesbtn_4.clicked.connect(lambda: self.ui.stackedWidget_5.setCurrentIndex(0))
            self.ui.returnbtn_4.clicked.connect(lambda: self.ui.stackedWidget_5.setCurrentIndex(1))
            self.ui.interestbtn_4.clicked.connect(lambda: self.ui.stackedWidget_5.setCurrentIndex(2))
        except Exception as e:
            print(f"An error occurred in update_charts: {e}")
            self.show_message_box("Error", f"An error occurred while updating charts: {e}")

    def clear_layout(self, layout):
        """Helper function to clear a layout."""
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()

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
