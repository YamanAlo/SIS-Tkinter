import customtkinter
from tkinter import messagebox, simpledialog, Menu
from tkinter import ttk
from database import StudentInfoSystem
import CTkMessagebox as msg
import languagepack
from course_list import CourseListWindow
import sqlite3

class CourseManagementWindow(customtkinter.CTkToplevel):
    def __init__(self, dashboard_window):
        super().__init__()
        self.dashboard_window = dashboard_window
        self.il8n = self.dashboard_window.il8n
        self.title(self.il8n.course_management)
        self.geometry("600x400")
        self.grab_set()
        self.db = StudentInfoSystem()
        self.resizable(False, False)


       
        self.student_label = customtkinter.CTkLabel(self, text=self.il8n.student_id)
        self.student_label.pack(pady=5)

        
        self.student_combobox = ttk.Combobox(self)
        self.student_combobox.set(self.il8n.select_student_id)
        self.student_combobox.pack(pady=5)
        self.populate_student_combobox()


        self.course_name_label = customtkinter.CTkLabel(self, text= self.il8n.course_name)
        self.course_name_label.pack(pady=10)
        self.course_name_entry = customtkinter.CTkEntry(self)
        self.course_name_entry.pack(pady=10)

        self.course_code_label = customtkinter.CTkLabel(self, text=self.il8n.course_code)
        self.course_code_label.pack(pady=10)
        self.course_code_entry = customtkinter.CTkEntry(self)
        self.course_code_entry.pack(pady=10)

        self.add_course_button = customtkinter.CTkButton(self, text=self.il8n.add_course, command=self.add_course)
        self.add_course_button.pack(pady=20)

        self.show_list_button = customtkinter.CTkButton(self, text=self.il8n.show_list, command=self.show_course_list)
        self.show_list_button.pack(pady=20)

        


    def clear_entries(self):
        self.course_name_entry.delete(0, 'end')
        self.course_code_entry.delete(0, 'end')

    def populate_student_combobox(self):
        students = self.db.get_students()
        student_ids = [str(student[0]) for student in students]
        self.student_combobox['values'] = ["Select Student ID"] + student_ids

    def add_course(self):
        course_name = self.course_name_entry.get()
        course_code = self.course_code_entry.get()
        student_id = self.student_combobox.get()


        
        if self.db.course_exists(course_name, course_code, student_id):
            msg.CTkMessagebox(title=self.il8n.error, message=self.il8n.course_already_exists, icon="cancel")
            return

        if not course_name or not course_code:
            msg.CTkMessagebox(title=self.il8n.error, message=self.il8n.enter_required_fields, icon="cancel")
            return

        if any(char.isdigit() for char in course_name):
            msg.CTkMessagebox(title=self.il8n.error, message=f"{self.il8n.course_name}{self.il8n.no_numbers}", icon="cancel")
            return
        
        # no spaces in course code
        if " " in course_code:
            msg.CTkMessagebox(title=self.il8n.error, message=f"{self.il8n.course_code}{self.il8n.no_spaces_allowed}", icon="cancel")
            return
        
        try:
            self.db.add_course(course_name, course_code, student_id)
            self.clear_entries()
            self.course_name_entry.focus()
            msg.CTkMessagebox(title=self.il8n.success, message=self.il8n.course_added_success, icon="check", option_1=self.il8n.thanks)
        except sqlite3.Error as e:
            msg.CTkMessagebox(title=self.il8n.error, message=f"{self.il8n.failed_add_course}: {str(e)}", icon="cancel")

    def show_course_list(self):
        course_list_window = CourseListWindow(self, self.db,self.dashboard_window.selected_language)
        course_list_window.show_course_list()   
        course_list_window.grab_set()
        course_list_window.wait_window()
        
    def update_language(self):
        self.il8n = self.dashboard_window.il8n
        self.title(self.il8n.course_management)
        self.course_name_label.configure(text=self.il8n.course_name)
        self.course_code_label.configure(text=self.il8n.course_code)
        self.add_course_button.configure(text=self.il8n.add_course)
        self.show_list_button.configure(text=self.il8n.show_list)
        self.student_label.configure(text=self.il8n.student_id)
        self.error_message = self.il8n.error
        self.required_fields_message = self.il8n.enter_required_fields
        self.no_spaces_allowed_message = self.il8n.no_spaces_allowed
        self.no_numbers_allowed_message = self.il8n.no_numbers
        self.course_added_success_message = self.il8n.course_added_success
        self.failed_add_course_message = self.il8n.failed_add_course
        self.error_message = self.il8n.error
        self.thanks_message = self.il8n.thanks
        self.success_message = self.il8n.success
        self.course_name_already_exists_message = self.il8n.course_name_already_exists
        self.code_already_exists_message = self.il8n.code_already_exists
        self.name_code_already_exists_message = self.il8n.name_code_already_exists
        self.course_already_exists_message = self.il8n.course_already_exists








 


