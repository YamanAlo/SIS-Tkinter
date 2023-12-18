# main.py

import customtkinter
import tkinter as tk
import sqlite3
import CTkMessagebox as msg
from student import StudentManagementWindow
from course import CourseManagementWindow
from department import DepartmentManagementWindow
from settings import SettingsWindow
import database
import languagepack

class DashboardWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.db = database.StudentInfoSystem()
        self.il8n = languagepack.I18N(language='en')  # Default language is set to English
        self.title(self.il8n.dashboard)
        
        
        self.create_widgets()

    def create_widgets(self):
        # button for creating the database and use the translation
        self.create_db_button = customtkinter.CTkButton(self, text=self.il8n.create_database, command=self.create_db)
        self.create_db_button.pack(pady=10)

        # Button for Student Management
        self.student_mgmt_button = customtkinter.CTkButton(self, text=self.il8n.student_management, command=self.open_student_mgmt)
        self.student_mgmt_button.pack(pady=10)

        # Button for Course Management
        self.course_mgmt_button = customtkinter.CTkButton(self, text=self.il8n.course_management, command=self.open_course_mgmt)
        self.course_mgmt_button.pack(pady=10)

        # Button for Department Management
        self.dept_mgmt_button = customtkinter.CTkButton(self, text=self.il8n.department_management, command=self.open_dept_mgmt)
        self.dept_mgmt_button.pack(pady=10)

        # Button for Clear Database
        self.clear_db_button = customtkinter.CTkButton(self, text=self.il8n.clear_database, command=self.clear_db)
        self.clear_db_button.pack(pady=10)

        # Button for Settings
        self.settings_button = customtkinter.CTkButton(self, text=self.il8n.settings, command=self.open_settings)
        self.settings_button.pack(pady=10)

    def open_student_mgmt(self):
        self.student_mgmt_window = StudentManagementWindow()
        
    def open_course_mgmt(self):
        self.course_mgmt_window = CourseManagementWindow()

    def open_dept_mgmt(self):
        self.dept_mgmt_window = DepartmentManagementWindow()

    def create_db(self):
        try:
            self.db.create_database()
            msg.CTkMessagebox(title=self.il8n.database_info, message=self.il8n.database_created, icon="check", option_1=self.il8n.thanks)
        except sqlite3.Error as err:
            msg.CTkMessagebox(title=self.il8n.database_info, message=self.il8n.failed_create_database, icon="cancel" + str(err))
        

    def clear_db(self):
        try:
            self.db.clear_database()
            msg.CTkMessagebox(title=self.il8n.database_info, message=self.il8n.clear_database, icon="check", option_1=self.il8n.thanks)
        except sqlite3.Error as err:
            msg.CTkMessagebox(title=self.il8n.database_info, message=self.il8n.failed_clear_database, icon="cancel" + str(err))

    def open_settings(self):
        self.settings_window = SettingsWindow(self)

    def update_language(self, language):
        self.il8n = languagepack.I18N(language=language)
        self.title(self.il8n.dashboard)
        self.create_db_button.configure(text=self.il8n.create_database)
        self.student_mgmt_button.configure(text=self.il8n.student_management)
        self.course_mgmt_button.configure(text=self.il8n.course_management)
        self.clear_db_button.configure(text=self.il8n.clear_database)
        self.settings_button.configure(text=self.il8n.settings)
        self.dept_mgmt_button.configure(text=self.il8n.enrollment_management)

        # Call update_language for other windows
       


            
# Create and run the dashboard
app = DashboardWindow()

app.mainloop()
