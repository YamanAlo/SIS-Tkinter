import customtkinter
from tkinter import messagebox, simpledialog, Menu
from tkinter import ttk
from database import StudentInfoSystem
import CTkMessagebox as msg
import languagepack

class CourseListWindow(customtkinter.CTkToplevel):
    def __init__(self, parent, db):
        super().__init__(parent)
        self.title("Course List")
        self.geometry("400x300")
        self.parent = parent
        self.db = db  # Pass the database connection from the parent
        self.il8n = languagepack.I18N(language='en')  # Default language is set to English

        # Frame for displaying the list of courses
        self.course_list_frame = customtkinter.CTkFrame(self)
        self.course_list_frame.pack(pady=20)

    def show_course_list(self):
        # Clear existing items in the frame
        for widget in self.course_list_frame.winfo_children():
            widget.destroy()

        # Populate the frame with course list from the database
        courses = self.db.get_courses()
        for course in courses:
            label_text = f"Course Name: {course[1]}, Course Code: {course[2]}"
            label = customtkinter.CTkLabel(self.course_list_frame, text=label_text)
            label.bind("<Button-3>", lambda event, id=course[0]: self.show_context_menu(event, id))
            label.pack()

    def show_context_menu(self, event, course_id):
        context_menu = Menu(self, tearoff=0)
        context_menu.add_command(label="Edit", command=lambda: self.edit_course(course_id))
        context_menu.add_command(label="Delete", command=lambda: self.delete_course(course_id))
        context_menu.post(event.x_root, event.y_root)

    def edit_course(self, course_id):
        course_details = self.db.get_courses()  # Replace with the appropriate method to get all courses
        selected_course = next((course for course in course_details if course[0] == course_id), None)

        if selected_course:
            # Store the currently selected course_id
            self.selected_course_id = course_id

            # Create a new window for editing
            edit_window = customtkinter.CTkToplevel(self)
            edit_window.title("Edit Course")
            edit_window.geometry("750x200")

            # Frame for course name and code entry
            entry_frame = customtkinter.CTkFrame(edit_window)
            entry_frame.pack(pady=10)

            # Course Name
            course_name_label = customtkinter.CTkLabel(entry_frame, text="Course Name:")
            course_name_label.pack(side='left', padx=5)
            new_name_entry = customtkinter.CTkEntry(entry_frame)
            new_name_entry.insert(0, selected_course[1])  # Pre-fill with existing value
            new_name_entry.pack(side='left', padx=5)

            # Course Code
            course_code_label = customtkinter.CTkLabel(entry_frame, text="Course Code:")
            course_code_label.pack(side='left', padx=5)
            new_code_entry = customtkinter.CTkEntry(entry_frame)
            new_code_entry.insert(0, selected_course[2])  # Pre-fill with existing value
            new_code_entry.pack(side='left', padx=5)

            # Save Changes Button
            save_button = customtkinter.CTkButton(edit_window, text="Save Changes",
                                                  command=lambda: self.save_changes(edit_window, course_id,
                                                                                   new_name_entry.get(),
                                                                                   new_code_entry.get()))
            save_button.pack(pady=10)

    def save_changes(self, edit_window, course_id, new_name, new_code):
        # Validate data entry
        if not new_name or not new_code:
            msg.CTkMessagebox(title = "Error", message= "Please enter both Course Name and Course Code." , icon = "cancel")
            return

        # Validate course name (no numbers allowed)
        if any(char.isdigit() for char in new_name):
            msg.CTkMessagebox(title = "Error", message = "Course Name should not contain numbers.", icon = "cancel")
            return

        try:
            self.db.update_course(course_id, new_name, new_code, "")
            msg.CTkMessagebox(title = "Success",message= "Course updated successfully.", icon = "check", option_1 = "Thanks")
            self.show_course_list()  # Refresh the course list after update
            edit_window.destroy()  # Close the edit window
        except Exception as e:
            messagebox.showerror(title= "Error", message= "Failed to update course.", icon = "cancel")


    def delete_course(self, course_id):
        confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this course?")
        if confirm:
            try:
                self.db.delete_course(course_id)
                messagebox.showinfo("Success", "Course deleted successfully.")
                self.show_course_list()  # Refresh the course list after deletion
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete course: {str(e)}")


class CourseManagementWindow(customtkinter.CTkToplevel):
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

        # Show List Button
        self.show_list_button = customtkinter.CTkButton(self, text="Show List", command=self.show_course_list)
        self.show_list_button.pack(pady=20)

        # Create the database connection
        self.db = StudentInfoSystem()

    def add_course(self):
        course_name = self.course_name_entry.get()
        course_code = self.course_code_entry.get()

        # Validate data entry
        if not course_name or not course_code:
            msg.CTkMessagebox(title="Error", message="Please enter both Course Name and Course Code.", icon="cancel")
            return

        # Validate course name (no numbers allowed)
        if any(char.isdigit() for char in course_name):
            msg.CTkMessagebox(title = "Error", message= "Course Name should not contain numbers.", icon = "cancel")
            return

        # Add course to the database
        try:
            self.db.add_course(course_name, course_code, "")
            msg.CTkMessagebox(title= "Success",message= "Course added successfully.", icon="check", option_1="Thanks")
        except Exception as e:
            msg.CTkMessagebox(title="Error", message= f"Failed to add course: {str(e)}", icon="cancel")

    def show_course_list(self):
        course_list_window = CourseListWindow(self, self.db)
        course_list_window.show_course_list()













 

      

