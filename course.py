import customtkinter

class CourseManagementWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Course Management")
        self.geometry("600x500")

        # Course Name
        self.course_name_label = customtkinter.CTkLabel(self, text="Course Name")
        self.course_name_label.pack(pady=10)
        self.course_name_entry = customtkinter.CTkEntry(self)
        self.course_name_entry.pack(pady=10)

        # Course Code
        self.course_code_label = customtkinter.CTkLabel(self, text="Course Code")
        self.course_code_label.pack(pady=10)
        self.course_code_entry = customtkinter.CTkEntry(self)
        self.course_code_entry.pack(pady=10)

        # Add Course Button
        self.add_course_button = customtkinter.CTkButton(self, text="Add Course", command=self.add_course)
        self.add_course_button.pack(pady=20)

        # Display area or list for courses
        # Implement a way to display existing courses

    def add_course(self):
        course_name = self.course_name_entry.get()
        course_code = self.teacher_name_entry.get()
        # Logic to add course to the database
        print(f"Adding Course: {course_name}, Course Code: {course_code}")