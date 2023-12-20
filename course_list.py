from tkinter import messagebox
from tkinter import Menu
import sqlite3
import CTkMessagebox as msg
import languagepack
import customtkinter


class CourseListWindow(customtkinter.CTkToplevel):
    def __init__(self, parent, db):
        super().__init__(parent)
        self.il8n = languagepack.I18N(language='en')
        self.title(self.il8n.course_list)
        self.geometry("400x300")
        self.parent = parent
        self.db = db




        self.course_list_frame = customtkinter.CTkFrame(self)
        self.course_list_frame.pack(pady=20)
        
   
    def show_course_list(self):
        for widget in self.course_list_frame.winfo_children():
            widget.destroy()

        courses = self.db.get_courses()
        for course in courses:
            label_text = f"{self.il8n.course_id}: {course[0]}, {self.il8n.course_name}: {course[1]}, {self.il8n.course_code}: {course[2]}"
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
            edit_window.title(self.il8n.edit_course)
            edit_window.geometry("750x200")
            edit_window.grab_set()

            entry_frame = customtkinter.CTkFrame(edit_window)
            entry_frame.pack(pady=10)

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
                                      command=lambda: (lambda: self.save_changes(edit_window, course_id,
                                                                                 new_name_entry.get(),
                                                                                 new_code_entry.get()))())
            save_button.pack(pady=10)

            

    def save_changes(self, edit_window, course_id, new_name, new_code):
        if not new_name or not new_code:
            msg.CTkMessagebox(title=self.il8n.error, message=self.il8n.enter_required_fields, icon="cancel")
            return

        if any(char.isdigit() for char in new_name):
            msg.CTkMessagebox(title=self.il8n.error, message=f"{self.il8n.course_name}{self.il8n.no_numbers}", icon="cancel")
            return
        
        if any(char.isspace() for char in new_name + new_code ):
            error_fields = [field for field, value in {"Course Name": new_name, "Course Code": new_code}.items() if any(char.isspace() for char in value)]
            error_message = f"{', '.join(error_fields)} {self.il8n.no_spaces_allowed}"
            msg.CTkMessagebox(title=self.il8n.error, message=error_message, icon="cancel")
            return

        try:
            self.db.update_course(course_id, new_name, new_code, "")
            msg.CTkMessagebox(title=self.il8n.success, message=self.il8n.course_updated_success, icon="check", option_1=self.il8n.thanks)
            self.show_course_list()
            self.grab_release()
            edit_window.destroy()
        except Exception as e:
            messagebox.showerror(title=self.il8n.error, message=f"{self.il8n.failed_add_course}: {str(e)}")

    def delete_course(self, course_id):
        confirm = messagebox.askyesno(self.il8n.confirm_deletion, self.il8n.are_you_sure_delete_course)
        if confirm:
            try:
                self.db.delete_course(course_id)
                messagebox.showinfo(self.il8n.success, self.il8n.course_deleted_successfully)
                self.show_course_list()
                self.grab_release()
            except Exception as e:
                messagebox.showerror(self.il8n.error, f"{self.il8n.failed_delete_course}: {str(e)}")