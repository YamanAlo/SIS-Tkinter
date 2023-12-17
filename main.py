import customtkinter 
import tkinter as tk
from tkinter import ttk
import sqlite3
import tkinter.messagebox as msg
import CTkMessagebox as msg
from student import StudentManagementWindow
from course import CourseManagementWindow
from grades import GradesManagementWindow
from attendance import AttendanceTrackingWindow
from settings import SettingsWindow
import database

class DashboardWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard")
        self.geometry("600x400")
        self.db = database.StudentInfoSystem()


        self.create_db_button = customtkinter.CTkButton(self, text="Create Database", command=self.Create_DB)
        self.create_db_button.pack(pady=10)


        # Button for Student Management
        self.student_mgmt_button = customtkinter.CTkButton(self, text="Student Management", command=self.open_student_mgmt)
        self.student_mgmt_button.pack(pady=10)

        # Button for Course Management
        self.course_mgmt_button = customtkinter.CTkButton(self, text="Course Management", command=self.open_course_mgmt)
        self.course_mgmt_button.pack(pady=10)

        # Button for Enrollment Management
        self.grades_mgmt_button = customtkinter.CTkButton(self, text="Enrollment Management", command=self.open_grades_mgmt)
        self.grades_mgmt_button.pack(pady=10)

        self.clear_db_button = customtkinter.CTkButton(self, text="Clear Database", command=self.clear_db)
        self.clear_db_button.pack(pady=10)

        # Button for Attendance Tracking
        

        # Button for Settings
        self.settings_button = customtkinter.CTkButton(self, text="Settings", command=self.open_settings)
        self.settings_button.pack(pady=10)

    def open_student_mgmt(self):
        self.student_mgmt_window = StudentManagementWindow()
        

    def open_course_mgmt(self):
        self.course_mgmt_window = CourseManagementWindow()
       

    def open_grades_mgmt(self):
        self.grades_mgmt_window = GradesManagementWindow()
        
    def Create_DB(self):
        try:
            self.db.create_database()
            msg.CTkMessagebox(title="Database Info", message="Database created.", icon="check", option_1="Thanks")
        except sqlite3.Error as err:
            msg.CTkMessagebox(title="Database Info", message="Failed to create the database", icon="cancel")

    def clear_db(self):
        try:
            self.db.clear_database()
            msg.CTkMessagebox(title="Database info", message="Database cleared.", icon="check", option_1="Thanks")
        except sqlite3.Error as err:
            msg.CTkMessagebox(title="Database info", message="Failed to clear the database.", icon="cancel")
        

    def open_settings(self):
        self.settings_window = SettingsWindow()
   

# Create and run the dashboard
app = DashboardWindow()
app.mainloop()
