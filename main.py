import customtkinter 


from student import StudentManagementWindow
from course import CourseManagementWindow
from grades import GradesManagementWindow
from attendance import AttendanceTrackingWindow
from settings import SettingsWindow
import database

class DashboardWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard")
        self.geometry("600x400")

        # Button for Student Management
        self.student_mgmt_button = customtkinter.CTkButton(self, text="Student Management", command=self.open_student_mgmt)
        self.student_mgmt_button.pack(pady=10)

        # Button for Course Management
        self.course_mgmt_button = customtkinter.CTkButton(self, text="Course Management", command=self.open_course_mgmt)
        self.course_mgmt_button.pack(pady=10)

        # Button for Grades Management
        self.grades_mgmt_button = customtkinter.CTkButton(self, text="Grades Management", command=self.open_grades_mgmt)
        self.grades_mgmt_button.pack(pady=10)

        # Button for Attendance Tracking
        self.attendance_button = customtkinter.CTkButton(self, text="Attendance Tracking", command=self.open_attendance)
        self.attendance_button.pack(pady=10)

        # Button for Settings
        self.settings_button = customtkinter.CTkButton(self, text="Settings", command=self.open_settings)
        self.settings_button.pack(pady=10)

    def open_student_mgmt(self):
        self.student_mgmt_window = StudentManagementWindow()
        

    def open_course_mgmt(self):
        self.course_mgmt_window = CourseManagementWindow()
       

    def open_grades_mgmt(self):
        self.grades_mgmt_window = GradesManagementWindow()
        
    def open_attendance(self):
        self.attendance_window = AttendanceTrackingWindow()
        

    def open_settings(self):
        self.settings_window = SettingsWindow()
   

# Create and run the dashboard
app = DashboardWindow()
app.mainloop()
