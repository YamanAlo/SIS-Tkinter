import customtkinter
from database import StudentInfoSystem

class GradesManagementWindow(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Enrollment Management")
        self.geometry("600x500")

        # Create an instance of StudentInfoSystem as an instance variable
        self.db = StudentInfoSystem()

        # Dropdowns for selecting student and course
        self.student_selector = customtkinter.CTkComboBox(self)
        self.populate_student_selector()  # Call method to populate student dropdown
        self.student_selector.pack(pady=5)

        self.course_selector = customtkinter.CTkComboBox(self)
        self.populate_course_selector()  # Call method to populate course dropdown
        self.course_selector.pack(pady=5)

        # Button to enroll the student
        self.enroll_student_button = customtkinter.CTkButton(self, text="Enroll Student", command=self.enroll_student)
        self.enroll_student_button.pack(pady=10)

    def populate_student_selector(self):
        students = self.db.get_students()
        student_ids = [str(student[0]) for student in students]
        self.student_selector.set(student_ids)

    def populate_course_selector(self):
        courses = self.db.get_courses()
        course_ids = [str(course[0]) for course in courses]
        self.course_selector.set(course_ids)

    def enroll_student(self):
        student_id = self.student_selector.get()
        course_id = self.course_selector.get()
        
        if not student_id or not course_id:
            print("Error: Please select a student and a course.")
            return

        self.db.add_enrollment(student_id, course_id)
        print(f"Enrolled Student {student_id} in Course {course_id}")

 

