from tkinter import messagebox
from tkinter import Menu
import sqlite3
import CTkMessagebox as msg
import languagepack
import customtkinter
import tkinter as tk
from tkinter import ttk

class CourseListWindow(customtkinter.CTkToplevel):
    def __init__(self, parent, db, language):
        super().__init__(parent)
        self.il8n = languagepack.I18N(language=language)
        self.title(self.il8n.show_list_title)
        self.geometry("500x300")
        self.parent = parent
        self.db = db



        self.course_list_frame = customtkinter.CTkFrame(self)
        self.course_list_frame.pack(pady=20)
        
   
    def show_course_list(self):
        for widget in self.course_list_frame.winfo_children():
            widget.destroy()

        courses = self.db.get_courses()
        for course in courses:
            label_text = f"{self.il8n.course_id}: {course[0]}, {self.il8n.course_name}: {course[1]}, {self.il8n.course_code}: {course[2]}, {self.il8n.student_id}: {course[3]}"
            label = customtkinter.CTkLabel(self.course_list_frame, text=label_text)
            label.bind("<Button-3>", lambda event, id=course[0]: self.show_context_menu(event, id))
            label.pack()

            self.grab_set()
     

        
    def show_context_menu(self, event, course_id):
        context_menu = Menu(self, tearoff=0)
        context_menu.add_command(label=self.il8n.edit, command=lambda: self.edit_course(course_id))
        context_menu.add_command(label=self.il8n.delete, command=lambda: self.delete_course(course_id))
        context_menu.post(event.x_root, event.y_root)

    def edit_course(self, course_id):
        course_details = self.db.get_courses()
        selected_course = next((course for course in course_details if course[0] == course_id), None)

        if selected_course:
            self.selected_course_id = course_id
        
            edit_window = customtkinter.CTkToplevel(self)
            edit_window.title(self.il8n.edit_course_title)
            edit_window.geometry("850x200")
            edit_window.grab_set()

            entry_frame = customtkinter.CTkFrame(edit_window)
            entry_frame.pack(pady=10)

            student_id_label = customtkinter.CTkLabel(entry_frame, text=f"{self.il8n.student_id}")
            student_id_label.pack(side='left', padx=5)
            student_id_combobox = ttk.Combobox(entry_frame)
            student_id_combobox['values'] = [str(student[0]) for student in self.db.get_students()]            
            student_id_combobox.set(self.il8n.select_student_id)
            student_id_combobox.pack(side='left', padx=5)
        

            course_id_label = customtkinter.CTkLabel(entry_frame, text=f"{self.il8n.course_id}")
            course_id_label.pack(side='left', padx=5)
            course_id_entry = customtkinter.CTkEntry(entry_frame)
            course_id_entry.insert(0, selected_course[0])
            course_id_entry.pack(side='left', padx=5)


            course_name_label = customtkinter.CTkLabel(entry_frame, text=f"{self.il8n.course_name}:")
            course_name_label.pack(side='left', padx=5)
            new_name_entry = customtkinter.CTkEntry(entry_frame)
            new_name_entry.insert(0, selected_course[1])
            new_name_entry.pack(side='left', padx=5)

            course_code_label = customtkinter.CTkLabel(entry_frame, text=f"{self.il8n.course_code}:")
            course_code_label.pack(side='left', padx=5)
            new_code_entry = customtkinter.CTkEntry(entry_frame)
            new_code_entry.insert(0, selected_course[2])
            new_code_entry.pack(side='left', padx=5)
            save_button = customtkinter.CTkButton(edit_window, text=self.il8n.save_changes,
                                      command=lambda: self.save_changes(edit_window, course_id,
                                                                                 new_name_entry.get(),
                                                                                 new_code_entry.get(),
                                                                                 student_id_combobox.get()))
            save_button.pack(pady=10)

            

    def save_changes(self, edit_window, course_id, new_name, new_code, new_student_id):
        if not new_name or not new_code or not new_student_id:
            msg.CTkMessagebox(title=self.il8n.error, message=self.il8n.enter_required_fields, icon="cancel")
            return

        if any(char.isdigit() for char in new_name):
            msg.CTkMessagebox(title=self.il8n.error, message=f"{self.il8n.course_name}{self.il8n.no_numbers}", icon="cancel")
            return
        
        # no spaces in course code
        if " " in new_code:
            msg.CTkMessagebox(title=self.il8n.error, message=f"{self.il8n.course_code}{self.il8n.no_spaces_allowed}", icon="cancel")
            return
        

        try:
            self.db.update_course(course_id, new_name, new_code, new_student_id)
            msg.CTkMessagebox(title=self.il8n.success, message=self.il8n.course_updated_success, icon="check", option_1=self.il8n.thanks)
            self.show_course_list()
            self.grab_release()
            edit_window.destroy()
        except sqlite3.Error as e:
            messagebox.showerror(title=self.il8n.error, message=f"{self.il8n.failed_update_course}: {str(e)}")

    def delete_course(self, course_id):
        confirm = messagebox.askyesno(self.il8n.confirm_deletion, self.il8n.are_you_sure_delete_course)
        if confirm:
            try:
                self.db.delete_course(course_id)
                messagebox.showinfo(self.il8n.success, self.il8n.course_deleted_successfully)
                self.show_course_list()
                self.grab_release()
            except sqlite3.Error as e:
                messagebox.showerror(self.il8n.error, f"{self.il8n.failed_delete_course}: {str(e)}")

    def update_language(self):
        self.il8n = self.dashboard_window.il8n
        self.title(self.il8n.show_list_title)
        self.edit_course_title = self.il8n.edit_course_title
        self.course_id = self.il8n.course_id
        self.course_name = self.il8n.course_name
        self.course_code = self.il8n.course_code
        self.edit = self.il8n.edit
        self.delete = self.il8n.delete
        self.confirm_deletion = self.il8n.confirm_deletion
        self.are_you_sure_delete_course = self.il8n.are_you_sure_delete_course
        self.success = self.il8n.success
        self.course_deleted_successfully = self.il8n.course_deleted_successfully
        self.failed_delete_course = self.il8n.failed_delete_course
        self.failed_update_course = self.il8n.failed_update_course
        self.enter_required_fields = self.il8n.enter_required_fields
        self.save_changes = self.il8n.save_changes
        self.course_updated_success = self.il8n.course_updated_success
        self.thanks = self.il8n.thanks
        self.failed_update_course = self.il8n.failed_update_course
        self.course_name_already_exists = self.il8n.course_name_already_exists
        self.code_already_exists = self.il8n.code_already_exists
        self.name_code_already_exists = self.il8n.name_code_already_exists
        self.select_student_id = self.il8n.select_student_id
        self.no_spaces_allowed = self.il8n.no_spaces_allowed
        self.no_numbers = self.il8n.no_numbers
        
