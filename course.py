import customtkinter
from tkinter import messagebox, simpledialog, Menu
from tkinter import ttk
from database import StudentInfoSystem
import CTkMessagebox as msg
import languagepack
from course_list import CourseListWindow


class CourseManagementWindow(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.il8n = languagepack.I18N(language='en')
        self.title(self.il8n.course_management)
        self.geometry("600x375")
        self.grab_set()

        
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

        self.db = StudentInfoSystem()

    def add_course(self):
        course_name = self.course_name_entry.get()
        course_code = self.course_code_entry.get()

        if not course_name or not course_code:
            msg.CTkMessagebox(title=self.il8n.error, message=self.il8n.enter_required_fields, icon="cancel")
            return

        if any(char.isdigit() for char in course_name):
            msg.CTkMessagebox(title=self.il8n.error, message=f"{self.il8n.course_name}{self.il8n.no_numbers}", icon="cancel")
            return
        
        # no spaces in both course name and course code
        if any(char.isspace() for char in course_name + course_code ):
            error_fields = [field for field, value in {"Course Name": course_name, "Course Code": course_code}.items() if any(char.isspace() for char in value)]
            error_message = f"{', '.join(error_fields)} {self.il8n.no_spaces_allowed}"
            msg.CTkMessagebox(title=self.il8n.error, message=error_message, icon="cancel")
            return
        try:
            self.db.add_course(course_name, course_code, "")
            msg.CTkMessagebox(title=self.il8n.success, message=self.il8n.course_added_success, icon="check", option_1=self.il8n.thanks)
        except Exception as e:
            msg.CTkMessagebox(title=self.il8n.error, message=f"{self.il8n.failed_add_course}: {str(e)}", icon="cancel")

    def show_course_list(self):
        course_list_window = CourseListWindow(self, self.db)
        course_list_window.show_course_list()   
        course_list_window.grab_set()
        course_list_window.wait_window()
        








 


