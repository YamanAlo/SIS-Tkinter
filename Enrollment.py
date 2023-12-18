# Enrollment.py
import customtkinter as ctk
from tkinter import ttk, Menu
import CTkMessagebox as msg
from database import StudentInfoSystem


class EnrollmentManagementWindow(ctk.CTkToplevel):
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
        self.course_combobox.set(" Choose Course Code")
        self.course_combobox.pack(pady=5)
        self.populate_course_combobox()

        # Button to enroll the student
        self.enroll_student_button = ctk.CTkButton(self, text="Enroll Student", command=self.enroll_student)
        self.enroll_student_button.pack(pady=10)

        # Button to show the list of enrollments
        self.show_list_button = ctk.CTkButton(self, text="Show List", command=self.show_enrollment_list)
        self.show_list_button.pack(pady=10)

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

    def show_enrollment_list(self):
        # Get enrollment list from the database
        enrollment_list = self.db.get_enrollment()

        # Open a new window to display the list
        EnrollmentListWindow(self, enrollment_list)




class EnrollmentListWindow(ctk.CTkToplevel):
    def __init__(self, parent, enrollment_list):
        super().__init__(parent)
        self.title("Enrollment List")
        self.geometry("400x300")
        self.parent = parent
        self.enrollment_list = enrollment_list

        # Frame for displaying the list of enrollments
        self.enrollment_list_frame = ctk.CTkFrame(self)
        self.enrollment_list_frame.pack(pady=20)

        # Show the enrollment list in the frame
        self.show_enrollment_list()

    def show_enrollment_list(self):
        # Clear existing items in the frame
        for widget in self.enrollment_list_frame.winfo_children():
            widget.destroy()

        # Populate the frame with enrollment list from the provided data
        for enrollment in self.enrollment_list:
            label_text = f"Student ID: {enrollment[0]}, Course Code: {enrollment[1]}"
            label = ctk.CTkLabel(self.enrollment_list_frame, text=label_text)
            label.bind("<Button-3>", lambda event, id=enrollment[0]: self.show_context_menu(event, id))
            label.pack()

    def show_context_menu(self, event, enrollment_id):
        context_menu = Menu(self, tearoff=0)
        context_menu.add_command(label="Edit", command=lambda: self.edit_enrollment(enrollment_id))
        context_menu.add_command(label="Delete", command=lambda: self.delete_enrollment(enrollment_id))
        context_menu.post(event.x_root, event.y_root)

    def edit_enrollment(self, enrollment_id):
        # Fetch the specific enrollment data based on enrollment_id using your get_enrollment method
        # Replace the following line with the appropriate logic
        enrollment_data = self.parent.db.get_enrollment()

        if enrollment_data:
            # Store the currently selected enrollment_id
            self.selected_enrollment_id = enrollment_id

            # Create a new window for editing
            edit_window = ctk.CTkToplevel(self)
            edit_window.title("Edit Enrollment")
            edit_window.geometry("700x200")

            # Frame for student and course selection
            entry_frame = ctk.CTkFrame(edit_window)
            entry_frame.pack(pady=10)

            # Edit Student ID
            student_id_label = ctk.CTkLabel(entry_frame, text="Edit Student ID:")
            student_id_label.pack(side='left', padx=5)
            new_student_id_combobox = ttk.Combobox(entry_frame, state="readonly")
            new_student_id_combobox['values'] =  [str(student[0]) for student in self.parent.db.get_students()]
            new_student_id_combobox.set("New Student ID ")
            new_student_id_combobox.pack(side='left', padx=5)

            # Edit Course Code
            course_code_label = ctk.CTkLabel(entry_frame, text="Edit Course Code:")
            course_code_label.pack(side='left', padx=5)
            new_course_code_combobox = ttk.Combobox(entry_frame, state="readonly")
            new_course_code_combobox['values'] =  [str(course[2]) for course in self.parent.db.get_courses()]
            new_course_code_combobox.set("New Course Code")
            new_course_code_combobox.pack(side='left', padx=5)

            # Save Changes Button
            save_button = ctk.CTkButton(edit_window, text="Save Changes",
                                        command=lambda: self.save_changes(edit_window, enrollment_id,
                                                                        new_student_id_combobox.get(),
                                                                        new_course_code_combobox.get()))
            save_button.pack(pady=10)


    def save_changes(self, edit_window, enrollment_id, new_student_id, new_course_code):
            try:
                # Fetch the specific enrollment data based on enrollment_id
                enrollment_data = self.parent.db.get_enrollment_by_id(enrollment_id)

                # Check if the enrollment data exists
                if enrollment_data:
                    # Update the enrollment using the provided data
                    self.parent.db.update_enrollment(enrollment_id, new_student_id, new_course_code)
                    msg.CTkMessagebox(title="Success", message="Changes saved successfully.", icon="info")
                    edit_window.destroy()  # Close the edit window
                    self.show_enrollment_list()  # Refresh the enrollment list in the main window
                else:
                    msg.CTkMessagebox(title="Error", message=f"Enrollment not found for ID {enrollment_id}.", icon="cancel")

            except Exception as e:
                msg.CTkMessagebox(title="Error", message=f"Failed to save changes: {str(e)}", icon="cancel")
                



    def delete_enrollment(self, enrollment_id):
        try:
            # Delete the enrollment using the provided enrollment_id
            self.parent.db.delete_enrollment(enrollment_id)
            msg.CTkMessagebox(title="Success", message="Enrollment deleted successfully.", icon="info")
            self.show_enrollment_list()
            self.parent.populate_student_combobox()  # Update the student combo box in the main window
            self.parent.populate_course_combobox()  # Update the course combo box in the main window

        except Exception as e:
            msg.CTkMessagebox(title="Error", message=f"Failed to delete enrollment: {str(e)}", icon="cancel")
