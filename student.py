import customtkinter as ctk
from tkinter import messagebox, simpledialog, Menu
from tkinter import ttk
from database import StudentInfoSystem
import CTkMessagebox as msg
import languagepack
from student_list import StudentListWindow
import sqlite3
        
class StudentManagementWindow(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry("900x650")
        self.il8n = languagepack.I18N(language='ar')
        self.title(self.il8n.student_management)
        self.grab_set()
    
        # Student ID
        self.student_id_label = ctk.CTkLabel(self, text=self.il8n.student_id)
        self.student_id_label.pack(pady=5)
        self.student_id_entry = ctk.CTkEntry(self)
        self.student_id_entry.pack(pady=5)

        # First Name
        self.first_name_label = ctk.CTkLabel(self, text=self.il8n.first_name)
        self.first_name_label.pack(pady=5)
        self.first_name_entry = ctk.CTkEntry(self)
        self.first_name_entry.pack(pady=5)

        # Last Name
        self.last_name_label = ctk.CTkLabel(self, text=self.il8n.last_name)
        self.last_name_label.pack(pady=5)
        self.last_name_entry = ctk.CTkEntry(self)
        self.last_name_entry.pack(pady=5)

        # Email
        self.email_label = ctk.CTkLabel(self, text=self.il8n.email)
        self.email_label.pack(pady=5)
        self.email_entry = ctk.CTkEntry(self)
        self.email_entry.pack(pady=5)
        
        # Phone
        self.phone_label = ctk.CTkLabel(self, text=self.il8n.phone)
        self.phone_label.pack(pady=5)
        self.phone_entry = ctk.CTkEntry(self)
        self.phone_entry.pack(pady=5)
        
        # Address
        self.address_label = ctk.CTkLabel(self, text=self.il8n.address)
        self.address_label.pack(pady=5)
        self.address_entry = ctk.CTkEntry(self)
        self.address_entry.pack(pady=5)

        # City
        self.city_label = ctk.CTkLabel(self, text=self.il8n.city)
        self.city_label.pack(pady=5)
        self.city_entry = ctk.CTkEntry(self)
        self.city_entry.pack(pady=5)

        # Add Student Button
        self.add_student_button = ctk.CTkButton(self, text=self.il8n.add_student, command=self.add_student)
        self.add_student_button.pack(pady=10)

        # Show List Button
        self.show_list_button = ctk.CTkButton(self, text=self.il8n.show_list, command=self.show_students_list)
        self.show_list_button.pack(pady=10)

        # Create the database connection
        self.db = StudentInfoSystem()



    def clear_entries(self):
        self.student_id_entry.delete(0, 'end')
        self.first_name_entry.delete(0, 'end')
        self.last_name_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.phone_entry.delete(0, 'end')
        self.address_entry.delete(0, 'end')
        self.city_entry.delete(0, 'end')

    def add_student(self):
        student_id = self.student_id_entry.get()
        student_first_name = self.first_name_entry.get()
        student_last_name = self.last_name_entry.get()
        student_email = self.email_entry.get()
        student_phone = self.phone_entry.get()
        student_address = self.address_entry.get()
        student_city = self.city_entry.get()


        
        if not student_id or not student_first_name or not student_last_name or not student_email or not student_phone or not student_address or not student_city:
            msg.CTkMessagebox(title=self.il8n.error, message=self.il8n.required_fields, icon="cancel")
            return

        # cant have spaces in all fields
        if any(char.isspace() for char in student_id + student_first_name + student_last_name + student_email + student_phone + student_address + student_city):
            error_fields = [field for field, value in {"Student ID": student_id, "First Name": student_first_name, "Last Name": student_last_name, "Email": student_email, "Phone": student_phone, "Address": student_address, "City": student_city}.items() if any(char.isspace() for char in value)]
            error_message = f"{', '.join(error_fields)} {self.il8n.no_spaces_allowed}"
            msg.CTkMessagebox(title=self.il8n.error, message=error_message, icon="cancel")
            return
        # Validate (no numbers allowed)
        if any(char.isdigit() for char in student_first_name + student_last_name + student_address + student_city):
            error_fields = [field for field, value in {"First Name": student_first_name, "Last Name": student_last_name, "Address": student_address, "City": student_city}.items() if any(char.isdigit() for char in value)]
            error_message = f"{', '.join(error_fields)} {self.il8n.no_numbers_allowed}"
            msg.CTkMessagebox(title=self.il8n.error, message=error_message, icon="cancel")
            return

        if not student_id.isdigit():
            msg.CTkMessagebox(title=self.il8n.error, message=self.il8n.student_id_number, icon="cancel")
            return

        if not student_phone.isdigit():
            msg.CTkMessagebox(title=self.il8n.error, message=self.il8n.phone_number, icon="cancel")
            return

        if not student_first_name.isalpha():
            msg.CTkMessagebox(title=self.il8n.error, message=self.il8n.first_name_alpha, icon="cancel")
            return

        if not student_last_name.isalpha():
            msg.CTkMessagebox(title=self.il8n.error, message=self.il8n.last_name_alpha, icon="cancel")
            return

        if not all(char.isalnum() or char in ['@', '.'] for char in student_email):
            msg.CTkMessagebox(title=self.il8n.error, message=self.il8n.email_format, icon="cancel")
            return

        try:
            self.db.add_student(student_id, student_first_name, student_last_name, student_email, student_phone, student_address, student_city)
            self.grab_release()
            self.clear_entries()
            self.student_id_entry.focus_set()
            msg.CTkMessagebox(title=self.il8n.success, message=self.il8n.student_added_success, icon="check", option_1=self.il8n.thanks)
        except sqlite3.Error as e:
            msg.CTkMessagebox(title=self.il8n.error, message=f"{self.il8n.failed_add_student}:  {str(e)}", icon="cancel")

    def show_students_list(self):
        student_list_window = StudentListWindow(self, self.db)
        student_list_window.show_students_list()
        student_list_window.grab_set()
        student_list_window.wait_window()
       


