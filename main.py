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
from CTkTable import *

class DashboardWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.db = database.StudentInfoSystem()
        self.selected_language = 'en' 
        self.il8n = languagepack.I18N(language=self.selected_language)  
        self.title(self.il8n.dashboard)
        self.resizable(False, False)
        
        self.create_widgets()

    def set_apperance(self):
            if sm1_value.get() == 1:
                customtkinter.set_appearance_mode("dark")
            else:
                customtkinter.set_appearance_mode("light")

    
    def create_widgets(self):

        # Button for creating the database and use the translation
        self.create_db_button = customtkinter.CTkButton(self, text=self.il8n.create_database, command=self.create_db)
        self.create_db_button.pack(pady=10)
        self.create_db_button.configure(font=("Arial ",13))

        # Button for Student Management
        self.student_mgmt_button = customtkinter.CTkButton(self, text=self.il8n.student_management, command=self.open_student_mgmt)
        self.student_mgmt_button.pack(pady=10)
        self.student_mgmt_button.configure(font=("Arial ",13))

        # Button for Course Management
        self.course_mgmt_button = customtkinter.CTkButton(self, text=self.il8n.course_management, command=self.open_course_mgmt)
        self.course_mgmt_button.pack(pady=10)
        self.course_mgmt_button.configure(font=("Arial ",13))

        # Button for Department Management
        self.dept_mgmt_button = customtkinter.CTkButton(self, text=self.il8n.department_management, command=self.open_dept_mgmt)
        self.dept_mgmt_button.pack(pady=10)
        self.dept_mgmt_button.configure(font=("Arial ",13))

        # button for showing the list of students with their courses and departments
        self.show_list_button = customtkinter.CTkButton(self, text=self.il8n.show_list, command=self.show_list)
        self.show_list_button.pack(pady=10)
        self.show_list_button.configure(font=("Arial ",13))


        # Button for Clear Database
        self.clear_db_button = customtkinter.CTkButton(self, text=self.il8n.clear_database, command=self.clear_db)
        self.clear_db_button.pack(pady=10)
        self.clear_db_button.configure(font=("Arial ",13))

        # Button for Settings
        self.settings_button = customtkinter.CTkButton(self, text=self.il8n.settings, command=self.open_settings)
        self.settings_button.pack(pady=10)
        self.settings_button.configure(font=("Arial ",13))

        global sm1_value
        sm1_value = customtkinter.IntVar(value=1)
        self.sm1 = customtkinter.CTkSwitch(self, text=self.il8n.Switch_Theme, variable=sm1_value, command=self.set_apperance)
        self.sm1.pack(pady=10)
    
    def open_settings(self):
        
        self.settings_window = SettingsWindow(self)

    def open_student_mgmt(self):
        self.student_mgmt_window = StudentManagementWindow(self)    
        self.student_mgmt_window.update_language()
    


    def open_course_mgmt(self):
        self.course_mgmt_window = CourseManagementWindow(self)
        self.course_mgmt_window.update_language()


    def open_dept_mgmt(self):
        self.dept_mgmt_window = DepartmentManagementWindow(self)
        self.dept_mgmt_window.update_language()
    
    

    def show_list(self):
        
        self.show_list_window = customtkinter.CTkToplevel(self)
        self.show_list_window.title(self.il8n.show_list)
        self.show_list_window.geometry("600x400")

        
        value = self.db.show_list()
        headers = [f'{self.il8n.student_id}', f'{self.il8n.course_name}',f'{self.il8n.course_code}', f'{self.il8n.department_name}']
        rows = len(value)

        # Create a CTkTable with headers
        table = CTkTable(self.show_list_window, column=4, row=rows + 1, values=[headers] + value)
        table.pack(pady=10,fill = 'both')

    def create_db(self):
        try:
            self.db.create_database()
            msg.CTkMessagebox(title=self.il8n.database_info, message=self.il8n.database_created, icon="check", option_1=self.il8n.thanks)
        except sqlite3.Error as err:
            msg.CTkMessagebox(title=self.il8n.database_info,message= f"{self.il8n.failed_clear_database}: {err}", icon="cancel" )
        

    def clear_db(self):
        try:
            self.db.clear_database()
            msg.CTkMessagebox(title=self.il8n.database_info, message=self.il8n.clear_database, icon="check", option_1=self.il8n.thanks)
        except sqlite3.Error as err:
            msg.CTkMessagebox(title=self.il8n.database_info, message=f"{self.il8n.failed_clear_database}: {err}" , icon="cancel")

   

    def update_language(self, language):
        
        self.selected_language = language
        self.il8n = languagepack.I18N(language=self.selected_language)
        self.title(self.il8n.dashboard)
        self.create_db_button.configure(text=self.il8n.create_database)
        self.student_mgmt_button.configure(text=self.il8n.student_management)
        self.course_mgmt_button.configure(text=self.il8n.course_management)
        self.clear_db_button.configure(text=self.il8n.clear_database)
        self.settings_button.configure(text=self.il8n.settings)
        self.dept_mgmt_button.configure(text=self.il8n.department_management)
        self.sm1.configure(text=self.il8n.Switch_Theme)
        self.show_list_button.configure(text=self.il8n.show_list)


    

      
       


            

app = DashboardWindow()

app.mainloop()
