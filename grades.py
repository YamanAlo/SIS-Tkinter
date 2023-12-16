import customtkinter
import database
class GradesManagementWindow(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Grades Management")
        self.geometry("600x500")

        # Dropdowns or entry fields for selecting student and course
        # You'll need to populate these from your database
        self.student_selector = customtkinter.CTkComboBox(self)
        self.student_selector.pack(pady=5)

        self.course_selector = customtkinter.CTkComboBox(self)
        self.course_selector.pack(pady=5)

        # Entry for grade
        self.grade_entry = customtkinter.CTkEntry(self)
        self.grade_entry.pack(pady=5)

        # Button to assign/update grade
        self.assign_grade_button = customtkinter.CTkButton(self, text="Assign Grade", command=self.assign_grade)
        self.assign_grade_button.pack(pady=10)

    def assign_grade(self):
        student = self.student_selector.get()
        course = self.course_selector.get()
        grade = self.grade_entry.get()
        # Logic to assign grade in the database
        print(f"Assign Grade: {grade} for Student: {student} in Course: {course}")

# Opened from the Dashboard Window
