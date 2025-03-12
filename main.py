import sys
from interface import *
from Custom_Widgets.Widgets import *  # Import the loadJsonStyle function


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())



import sys
from interface import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect buttons to the update_active_tab method
        self.ui.dashbtn.clicked.connect(lambda: self.update_active_tab(self.ui.dashbtn, 0))
        self.ui.addbtn.clicked.connect(lambda: self.update_active_tab(self.ui.addbtn, 1))
        self.ui.removebtn.clicked.connect(lambda: self.update_active_tab(self.ui.removebtn, 2))
        self.ui.depositbtn.clicked.connect(lambda: self.update_active_tab(self.ui.depositbtn, 3))

        # Set the default active tab to dashboard
        self.update_active_tab(self.ui.dashbtn, 0)

        self.show()

    def update_active_tab(self, active_button, page_index):
        buttons = [self.ui.dashbtn, self.ui.addbtn, self.ui.removebtn, self.ui.depositbtn]
        icons_active = {
            self.ui.dashbtn: ":/coloredicons/assets/icons/blue/bar-chart.svg",
            self.ui.addbtn: ":/coloredicons/assets/icons/blue/plus.svg",
            self.ui.removebtn: ":/coloredicons/assets/icons/blue/x.svg",
            self.ui.depositbtn: ":/coloredicons/assets/icons/blue/folder-plus.svg"
        }
        icons_inactive = {
            self.ui.dashbtn: ":/whiteicons/assets/icons/white/bar-chart.svg",
            self.ui.addbtn: ":/whiteicons/assets/icons/white/plus.svg",
            self.ui.removebtn: ":/whiteicons/assets/icons/white/x.svg",
            self.ui.depositbtn: ":/whiteicons/assets/icons/white/folder-plus.svg"
        }

        for button in buttons:
            if button == active_button:
                button.setStyleSheet("""
                    background-color: #fefeff;
                    padding: 10px 5px;
                    text-align: left;
                    border-top-left-radius: 20px;
                    border: 2px solid #2596be;
                    color: #2596be;
                """)
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
