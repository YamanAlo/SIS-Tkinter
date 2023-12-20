import customtkinter
from tkinter import messagebox, simpledialog, Menu
from tkinter import ttk
from database import StudentInfoSystem
import CTkMessagebox as msg
import languagepack
import customtkinter
from tkinter import messagebox, Menu
from department_list import DepartmentListWindow

class DepartmentManagementWindow(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.il8n = languagepack.I18N(language='en')
        self.title(self.il8n.department_management)
        self.geometry("600x375")
        self.grab_set()
        self.db = StudentInfoSystem()

        self.create_widgets()

    def create_widgets(self):
        

        # student id 
        student_label = customtkinter.CTkLabel(self, text=self.il8n.student_id )
        student_label.pack(pady=5)

        # Combobox for selecting student
        self.student_combobox = ttk.Combobox(self)
        self.student_combobox.set(self.il8n.select_student_id)
        self.student_combobox.pack(pady=5)
        self.populate_student_combobox()
    

        self.add_department_label = customtkinter.CTkLabel(self, text=self.il8n.add_department)
        self.add_department_label.pack(pady=10)
        self.department_name_entry = customtkinter.CTkEntry(self)
        self.department_name_entry.pack(pady=10)

        # Add Department Button
        self.add_department_button = customtkinter.CTkButton(self, text=self.il8n.add_department, command=self.add_department)
        self.add_department_button.pack(pady=10)

        # Show Departments Button
        self.show_departments_button = customtkinter.CTkButton(self, text=self.il8n.show_departments, command=self.show_departments)
        self.show_departments_button.pack(pady=10)

       
    
    def populate_student_combobox(self):
        students = self.db.get_students()
        student_ids = [str(student[0]) for student in students]
        self.student_combobox['values'] = ["Select Student ID"] + student_ids

    def add_department(self):
        department_name = self.department_name_entry.get()
        student_id = self.student_combobox.get()

        if not department_name or not student_id:
            msg.CTkMessagebox(title=self.il8n.error, message=self.il8n.enter_required_fields, icon="cancel")
            return
        
        if any(char.isdigit() for char in department_name):
            msg.CTkMessagebox(title=self.il8n.error, message=f"{self.il8n.department_name}{self.il8n.no_numbers}", icon="cancel")
            return
        
        # no spaces in student id 
        if any(char.isspace() for char in student_id):
            error_fields = [field for field, value in {"Student ID": student_id}.items() if any(char.isspace() for char in value)]
            error_message = f"{', '.join(error_fields)} {self.il8n.no_spaces_allowed}"
            msg.CTkMessagebox(title=self.il8n.error, message=error_message, icon="cancel")
            return
        
        


        try:
            
            self.db.add_department(department_name, student_id)
            msg.CTkMessagebox(title=self.il8n.success, message=self.il8n.department_added_success, icon="check", option_1=self.il8n.thanks)
        except Exception as e:
            msg.CTkMessagebox(title=self.il8n.error, message=f"{self.il8n.failed_add_department}: {str(e)}", icon="cancel")

    def show_departments(self):
        
        department_list_window = DepartmentListWindow(self, self.db)
        department_list_window.show_departments()
        department_list_window.grab_set()
        department_list_window.wait_window()