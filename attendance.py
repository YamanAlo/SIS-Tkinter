import customtkinter
import database
class AttendanceTrackingWindow(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Attendance Tracking")
        self.geometry("600x500")

        # Dropdown or entry field for selecting student
        self.student_selector = customtkinter.CTkComboBox(self)
        self.student_selector.pack(pady=5)

        # Date selector for attendance
        # You might need a date picker widget or a simple entry
        self.date_entry = customtkinter.CTkEntry(self)
        self.date_entry.pack(pady=5)

        # Radio buttons or dropdown for attendance status (Present, Absent, etc.)
        self.status_selector = customtkinter.CTkComboBox(self, values=["Present", "Absent", "Late"])
        self.status_selector.pack(pady=5)

        # Button to record attendance
        self.record_button = customtkinter.CTkButton(self, text="Record Attendance", command=self.record_attendance)
        self.record_button.pack(pady=10)

    def record_attendance(self):
        student = self.student_selector.get()
        date = self.date_entry.get()
        status = self.status_selector.get()
        # Logic to record attendance in the database
        print(f"Record Attendance: {status} for Student: {student} on {date}")

# Opened from the Dashboard Window
