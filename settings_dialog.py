from PySide6.QtWidgets import (QDialog, QComboBox, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox, QCheckBox, QGroupBox, QMessageBox, QKeySequenceEdit, QStackedWidget, QListWidget, QFrame)
from PySide6.QtCore import Qt
import json
import os

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.settings = self.load_settings()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Settings")
        self.setMinimumWidth(300)
        self.setMinimumHeight(300)

        # Create main layout
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # Create navigation sidebar
        self.nav_list = QListWidget()
        self.nav_list.setMaximumWidth(200)
        self.nav_list.setStyleSheet("""
            QListWidget {
                background-color: #f0f0f0;
                border: none;
                border-radius: 5px;
            }
            QListWidget::item {
                padding: 10px;
                border-radius: 5px;
            }
            QListWidget::item:selected {
                background-color: #2596be;
                color: white;
            }
        """)
        main_layout.addWidget(self.nav_list)

        # Create stacked widget for settings pages
        self.stack = QStackedWidget()
        main_layout.addWidget(self.stack)

        # Add navigation items
        self.nav_items = [
            "Database Settings",
            "Application Settings",
            "Keyboard Shortcuts"
        ]
        self.nav_list.addItems(self.nav_items)
        self.nav_list.currentRowChanged.connect(self.stack.setCurrentIndex)

        # Create pages
        self.create_database_page()
        self.create_application_page()
        self.create_shortcuts_page()

        # Create button layout
        button_layout = QHBoxLayout()
        save_button = QPushButton("Save")
        save_button.setStyleSheet("""
            QPushButton {
                background-color: #2596be;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #1a7a9e;
            }
        """)
        cancel_button = QPushButton("Cancel")
        cancel_button.setStyleSheet("""
            QPushButton {
                background-color: #f0f0f0;
                color: #333;
                border: 1px solid #ddd;
                padding: 8px 16px;
                border-radius: 4px;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
        """)
        
        button_layout.addStretch()
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)
        
        # Add button layout to main layout
        main_layout.addLayout(button_layout)

        # Connect buttons
        save_button.clicked.connect(self.save_settings)
        cancel_button.clicked.connect(self.reject)

        # Set initial selection
        self.nav_list.setCurrentRow(0)

    def create_database_page(self):
        page = QFrame()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        # Database Settings Group
        db_group = QGroupBox("Database Settings")
        db_layout = QVBoxLayout()
        db_layout.setSpacing(15)

        # Host
        host_layout = QHBoxLayout()
        host_label = QLabel("Host:")
        self.host_edit = QLineEdit(self.settings.get('db_host', 'localhost'))
        host_layout.addWidget(host_label)
        host_layout.addWidget(self.host_edit)
        db_layout.addLayout(host_layout)

        # Database Name
        db_name_layout = QHBoxLayout()
        db_name_label = QLabel("Database Name:")
        self.db_name_edit = QLineEdit(self.settings.get('db_name', 'loan_management'))
        db_name_layout.addWidget(db_name_label)
        db_name_layout.addWidget(self.db_name_edit)
        db_layout.addLayout(db_name_layout)

        # Username
        username_layout = QHBoxLayout()
        username_label = QLabel("Username:")
        self.username_edit = QLineEdit(self.settings.get('db_user', 'root'))
        username_layout.addWidget(username_label)
        username_layout.addWidget(self.username_edit)
        db_layout.addLayout(username_layout)

        # Password
        password_layout = QHBoxLayout()
        password_label = QLabel("Password:")
        self.password_edit = QLineEdit(self.settings.get('db_password', 'akshat'))
        self.password_edit.setEchoMode(QLineEdit.Password)
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_edit)
        db_layout.addLayout(password_layout)

        db_group.setLayout(db_layout)
        layout.addWidget(db_group)
        layout.addStretch()
        self.stack.addWidget(page)

    def create_application_page(self):
        page = QFrame()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        # Application Settings Group
        app_group = QGroupBox("Application Settings")
        app_layout = QVBoxLayout()
        app_layout.setSpacing(15)

        # Interest Rate
        interest_layout = QHBoxLayout()
        interest_label = QLabel("Interest Rate (%):")
        self.interest_spin = QSpinBox()
        self.interest_spin.setRange(0, 100)
        self.interest_spin.setValue(self.settings.get('interest_rate', 36))
        interest_layout.addWidget(interest_label)
        interest_layout.addWidget(self.interest_spin)
        app_layout.addLayout(interest_layout)

        # Backup Settings
        backup_layout = QHBoxLayout()
        backup_label = QLabel("Backup Location:")
        self.backup_edit = QLineEdit(self.settings.get('backup_location', 'D:\\'))
        backup_layout.addWidget(backup_label)
        backup_layout.addWidget(self.backup_edit)
        app_layout.addLayout(backup_layout)

        # Auto Backup
        self.auto_backup_check = QCheckBox("Enable Auto Backup")
        self.auto_backup_check.setChecked(self.settings.get('auto_backup', False))
        app_layout.addWidget(self.auto_backup_check)

        # Backup Frequency
        frequency_layout = QHBoxLayout()
        frequency_label = QLabel("Backup Frequency (hours):")
        self.frequency_spin = QSpinBox()
        self.frequency_spin.setRange(1, 24)
        self.frequency_spin.setValue(self.settings.get('backup_frequency', 24))
        frequency_layout.addWidget(frequency_label)
        frequency_layout.addWidget(self.frequency_spin)
        app_layout.addLayout(frequency_layout)

        # Date Format
        date_format_layout = QHBoxLayout()
        date_format_label = QLabel("Date Format:")
        self.date_format_combo = QComboBox()
        self.date_format_combo.addItems(["YYYY-MM-DD", "DD-MM-YYYY", "MM/DD/YYYY"])
        self.date_format_combo.setCurrentText(self.settings.get('date_format', 'YYYY-MM-DD'))
        date_format_layout.addWidget(date_format_label)
        date_format_layout.addWidget(self.date_format_combo)
        app_layout.addLayout(date_format_layout)

        # Number Division
        number_division_layout = QHBoxLayout()
        number_division_label = QLabel("Number Division Factor:")
        self.number_division_spin = QSpinBox()
        self.number_division_spin.setRange(1, 1000)
        self.number_division_spin.setValue(self.settings.get('number_division', 1))
        self.number_division_spin.setToolTip("Divide displayed numbers by this factor (e.g., 10 for 1,00,000 to show as 10,000)")
        number_division_layout.addWidget(number_division_label)
        number_division_layout.addWidget(self.number_division_spin)
        app_layout.addLayout(number_division_layout)

        app_group.setLayout(app_layout)
        layout.addWidget(app_group)
        layout.addStretch()
        self.stack.addWidget(page)

    def create_shortcuts_page(self):
        page = QFrame()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        # Keyboard Shortcuts Group
        shortcuts_group = QGroupBox("Keyboard Shortcuts")
        shortcuts_layout = QVBoxLayout()
        shortcuts_layout.setSpacing(15)

        # Create shortcut editors
        self.shortcut_editors = {}
        shortcut_configs = {
            "Dashboard": "shortcut_dashboard",
            "Add Record": "shortcut_add_record",
            "Remove Record": "shortcut_remove_record",
            "Add Deposit": "shortcut_add_deposit",
            "View Records": "shortcut_view_records",
            "Accounts": "shortcut_accounts"
        }

        for label, setting_key in shortcut_configs.items():
            shortcut_layout = QHBoxLayout()
            shortcut_label = QLabel(f"{label}:")
            shortcut_edit = QKeySequenceEdit()
            shortcut_edit.setKeySequence(self.settings.get(setting_key, ""))
            shortcut_layout.addWidget(shortcut_label)
            shortcut_layout.addWidget(shortcut_edit)
            shortcuts_layout.addLayout(shortcut_layout)
            self.shortcut_editors[setting_key] = shortcut_edit

        shortcuts_group.setLayout(shortcuts_layout)
        layout.addWidget(shortcuts_group)
        layout.addStretch()
        self.stack.addWidget(page)

    def load_settings(self):
        """Load settings from the JSON file"""
        settings_file = "settings.json"
        if os.path.exists(settings_file):
            try:
                with open(settings_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading settings: {e}")
                return {}
        return {}

    def save_settings(self):
        """Save settings to the JSON file"""
        try:
            # Update settings dictionary with current values
            self.settings.update({
                'db_host': self.host_edit.text(),
                'db_name': self.db_name_edit.text(),
                'db_user': self.username_edit.text(),
                'db_password': self.password_edit.text(),
                'interest_rate': self.interest_spin.value(),
                'backup_location': self.backup_edit.text(),
                'auto_backup': self.auto_backup_check.isChecked(),
                'backup_frequency': self.frequency_spin.value(),
                'date_format': self.date_format_combo.currentText(),
                'number_division': self.number_division_spin.value(),
                'shortcut_dashboard': self.shortcut_editors['shortcut_dashboard'].keySequence().toString(),
                'shortcut_add_record': self.shortcut_editors['shortcut_add_record'].keySequence().toString(),
                'shortcut_remove_record': self.shortcut_editors['shortcut_remove_record'].keySequence().toString(),
                'shortcut_add_deposit': self.shortcut_editors['shortcut_add_deposit'].keySequence().toString(),
                'shortcut_view_records': self.shortcut_editors['shortcut_view_records'].keySequence().toString(),
                'shortcut_accounts': self.shortcut_editors['shortcut_accounts'].keySequence().toString()
            })

            # Save to file
            with open('settings.json', 'w') as f:
                json.dump(self.settings, f, indent=4)

            QMessageBox.information(self, "Success", "Settings saved successfully!")
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save settings: {str(e)}")
