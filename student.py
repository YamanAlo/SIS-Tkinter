import customtkinter
import database

class StudentManagementWindow(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Student Management")
        self.geometry("600x500")
        self.db = database.StudentInfoSystem()
        

        # Form Labels and Entry Widgets
        self.name_label = customtkinter.CTkLabel(self, text="Name")
        self.name_label.pack()
        self.name_entry = customtkinter.CTkEntry(self)
        self.name_entry.pack()

        # Similar setup for other fields like birthdate, gender, class

        # Add Student Button
        self.add_student_button = customtkinter.CTkButton(self, text="Add Student", command=self.add_student)
        self.add_student_button.pack(pady=10)

        # List or table to display students (can use CTkLabel, CTkEntry, CTkButton for interaction)

    def add_student(self):
        # Logic to add a new student
        name = self.name_entry.get()
        # Collect other field values similarly
        print(f"Add Student: {name}")

# This would be opened from the Dashboard Window
