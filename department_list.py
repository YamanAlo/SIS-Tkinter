import languagepack
import customtkinter
from tkinter import messagebox, Menu
import CTkMessagebox as msg
from tkinter import ttk
import sqlite3

class DepartmentListWindow(customtkinter.CTkToplevel):
    def __init__(self, parent, db, language):
        super().__init__(parent)
        self.il8n = languagepack.I18N(language= language)
        self.title(self.il8n.show_list_title)
        self.geometry("400x300")
        self.parent = parent
        self.db = db

        self.department_list_frame = customtkinter.CTkFrame(self)
        self.department_list_frame.pack(pady=20)

    def show_departments(self):
        for widget in self.department_list_frame.winfo_children():
            widget.destroy()
            

        departments = self.db.get_department()
        for department in departments:
            label_text = f"{self.il8n.department_id}: {department[0]}, {self.il8n.department_name}: {department[1]}, {self.il8n.student_id}: {department[2]}"
            label = customtkinter.CTkLabel(self.department_list_frame, text=label_text)
            label.bind("<Button-3>", lambda event, id=department[0]: self.show_context_menu(event, id))
            label.pack()

            self.grab_set()
      

    def show_context_menu(self, event, department_id):
        context_menu = Menu(self, tearoff=0)
        context_menu.add_command(label=self.il8n.edit, command=lambda: self.edit_department(department_id))
        context_menu.add_command(label=self.il8n.delete, command=lambda: self.delete_department(department_id))
        context_menu.post(event.x_root, event.y_root)

    def edit_department(self, department_id):
        department_details = self.db.get_department()
        selected_department = next((department for department in department_details if department[0] == department_id), None)

        if selected_department:
            self.selected_department_id = department_id

            edit_window = customtkinter.CTkToplevel(self)
            edit_window.title(self.il8n.edit_department_title)
            edit_window.geometry("750x200")
            edit_window.grab_set()

            entry_frame = customtkinter.CTkFrame(edit_window)
            entry_frame.pack(pady=10)

            department_id_label = customtkinter.CTkLabel(entry_frame, text=f"{self.il8n.department_id}")
            department_id_label.pack(side='left', padx=5)
            department_id_entry = customtkinter.CTkEntry(entry_frame)
            department_id_entry.insert(0, selected_department[0])
            department_id_entry.pack(side='left', padx=5)


            department_name_label = customtkinter.CTkLabel(entry_frame, text=f"{self.il8n.department_name}:")
            department_name_label.pack(side='left', padx=5)
            new_dept_entry = customtkinter.CTkEntry(entry_frame)
            new_dept_entry.insert(0, selected_department[1])  
            new_dept_entry.pack(side='left', padx=5)

            # show the student ids that are in the database in a combobox
            student_id_label = customtkinter.CTkLabel(entry_frame, text=self.il8n.edit_student_id)
            student_id_label.pack(side='left', padx=5)
            new_student_id_combobox = ttk.Combobox(entry_frame)
            new_student_id_combobox['values'] =  [str(student[0]) for student in self.db.get_students()]
            new_student_id_combobox.set("New Student ID ")
            new_student_id_combobox.pack(side='left', padx=5)


            save_button = customtkinter.CTkButton(edit_window, text=self.il8n.save_changes, command=lambda: 
                                                  self.save_changes(edit_window, department_id, new_dept_entry.get(), new_student_id_combobox.get()))
            
            save_button.pack(pady=10)

    def save_changes(self, edit_window, department_id, new_name, new_student_id):
        if not new_name or not new_student_id :
            msg.CTkMessagebox(title=self.il8n.error, message=self.il8n.enter_required_fields, icon="cancel")
            return
        

        try:
            self.db.update_department(department_id, new_name, new_student_id)
            msg.CTkMessagebox(title=self.il8n.success, message=self.il8n.department_updated_successfully, icon="check", option_1=self.il8n.thanks)
            self.show_departments()
            self.grab_release()
            edit_window.destroy()
        except sqlite3.Error as e:
           msg.CTkMessagebox(title=self.il8n.error, message=f"{self.il8n.failed_update_department}: {str(e)}, icon='cancel'")

    def delete_department(self, department_id):
        confirm = messagebox.askyesno(self.il8n.confirm_deletion, self.il8n.are_you_sure_delete_department)
        if confirm:
            try:
                self.db.delete_department(department_id)
                messagebox.showinfo(self.il8n.success, self.il8n.department_deleted_successfully)                
                self.show_departments()
                self.grab_release()
                
            except sqlite3.Error as e:
               messagebox.showerror(self.il8n.error, f"{self.il8n.failed_delete_department}: {str(e)}, icon='cancel'")


    def update_language(self, language):
        self.il8n = self.dashboard_window.il8n
        self.title(self.il8n.show_list_title)
        self.edit_department_title = self.il8n.edit_department_title
        self.edit_student_id = self.il8n.edit_student_id
        self.edit = self.il8n.edit
        self.delete = self.il8n.delete
        self.confirm_deletion = self.il8n.confirm_deletion
        self.are_you_sure_delete_department = self.il8n.are_you_sure_delete_department
        self.success = self.il8n.success
        self.department_deleted_successfully = self.il8n.department_deleted_successfully
        self.failed_delete_department = self.il8n.failed_delete_department
        self.failed_update_department = self.il8n.failed_update_department
        self.enter_required_fields = self.il8n.enter_required_fields
        self.save_changes = self.il8n.save_changes
        self.department_updated_successfully = self.il8n.department_updated_successfully
        self.thanks = self.il8n.thanks
        self.department_id = self.il8n.department_id
        self.department_name = self.il8n.department_name
        self.student_id = self.il8n.student_id
        self.show_list_title = self.il8n.show_list_title
        self.department_already_exists = self.il8n.department_already_exists
        self.department_already_exists_for_student = self.il8n.department_already_exists_for_student

        



