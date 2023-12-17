import customtkinter as ctk
from tkinter import ttk
from database import StudentInfoSystem
import CTkMessagebox as msg

class GradesManagementWindow(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Enrollment Management")
        self.geometry("600x500")

 
        self.db = StudentInfoSystem()

        # Labels for student and course selection
        student_label = ctk.CTkLabel(self, text="Select Student ID:")
        student_label.pack(pady=5)

        # Combobox for selecting student
        self.student_combobox = ttk.Combobox(self, state="readonly")
        self.student_combobox.set("Select Student ID")  
        self.student_combobox.pack(pady=5)
        self.populate_student_combobox()

        course_label = ctk.CTkLabel(self, text="Select Course Code:")
        course_label.pack(pady=5)

        # Combobox for selecting course
        self.course_combobox = ttk.Combobox(self, state="readonly")
        self.course_combobox.set("Select Course Code")
        self.course_combobox.pack(pady=5)  
        self.populate_course_combobox()

        # Button to enroll the student
        self.enroll_student_button = ctk.CTkButton(self, text="Enroll Student", command=self.enroll_student)
        self.enroll_student_button.pack(pady=10)

    def populate_student_combobox(self):
        students = self.db.get_students()
        student_ids = [str(student[0]) for student in students]
        self.student_combobox['values'] = ["Select Student ID"] + student_ids

    def populate_course_combobox(self):
        courses = self.db.get_courses()
        course_codes = [str(course[2]) for course in courses]
        self.course_combobox['values'] = ["Select Course Code"] + course_codes

    def enroll_student(self):
        student_id = self.student_combobox.get()
        course_code = self.course_combobox.get()

        if student_id == "Select Student ID" or course_code == "Select Course Code":
            msg.CTkMessagebox(title="Error", message="Please select a valid student and course.", icon="cancel")
            return

        if not student_id or not course_code:
            msg.CTkMessagebox(title="Error", message="Please select both student ID and course code.", icon="cancel")
            return

        try:
            self.db.add_enrollment(student_id, course_code)
            msg.CTkMessagebox(title="Success", message=f"Enrolled Student {student_id} in Course {course_code}", icon="info")
        except Exception as e:
            msg.CTkMessagebox(title="Error", message=f"Failed to enroll student: {str(e)}", icon="cancel")

