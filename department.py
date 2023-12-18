import customtkinter
from tkinter import messagebox, simpledialog, Menu
from tkinter import ttk
from database import StudentInfoSystem
import CTkMessagebox as msg
import languagepack



import customtkinter
from tkinter import messagebox, Menu

class DepartmentListWindow(customtkinter.CTkToplevel):
    def __init__(self, parent, db):
        super().__init__(parent)
        self.il8n = languagepack.I18N(language='en')
        self.title(self.il8n.department_list)
        self.geometry("400x300")
        self.parent = parent
        self.db = db

        self.department_list_frame = customtkinter.CTkFrame(self)
        self.department_list_frame.pack(pady=20)

    def show_departments(self):
        for widget in self.department_list_frame.winfo_children():
            widget.destroy()

        departments = self.db.get_departments()
        for department in departments:
            label_text = f"{self.parent.il8n.department_name}: {department[1]}, {self.parent.il8n.department_id}: {department[0]}"
            label = customtkinter.CTkLabel(self.department_list_frame, text=label_text)
            label.bind("<Button-3>", lambda event, id=department[0]: self.show_context_menu(event, id))
            label.pack()

    def show_context_menu(self, event, department_id):
        context_menu = Menu(self, tearoff=0)
        context_menu.add_command(label=self.parent.il8n.edit, command=lambda: self.edit_department(department_id))
        context_menu.add_command(label=self.parent.il8n.delete, command=lambda: self.delete_department(department_id))
        context_menu.post(event.x_root, event.y_root)

    def edit_department(self, department_id):
        edit_window = customtkinter.CTkToplevel(self)
        edit_window.title(self.parent.il8n.edit_department)
        edit_window.geometry("400x150")

        entry_frame = customtkinter.CTkFrame(edit_window)
        entry_frame.pack(pady=10)

        department_name_label = customtkinter.CTkLabel(entry_frame, text=f"{self.parent.il8n.department_name}:")
        department_name_label.pack(side='left', padx=5)
        new_name_entry = customtkinter.CTkEntry(entry_frame)
        new_name_entry.insert(0, self.db.get_department(department_id)[1])  # Assuming the name is at index 1
        new_name_entry.pack(side='left', padx=5)

        save_button = customtkinter.CTkButton(edit_window, text=self.parent.il8n.save_changes,
                                              command=lambda: self.save_changes(edit_window, department_id, new_name_entry.get()))
        save_button.pack(pady=10)

    def save_changes(self, edit_window, department_id, new_name):
        if not new_name:
            messagebox.showerror(title=self.parent.il8n.error, message=self.parent.il8n.enter_required_fields)
            return

        try:
            self.db.update_department(department_id, new_name)
            messagebox.showinfo(title=self.parent.il8n.success, message=self.parent.il8n.department_updated_successfully)
            self.show_departments()
            edit_window.destroy()
        except Exception as e:
            messagebox.showerror(title=self.parent.il8n.error, message=f"{self.parent.il8n.failed_update_department}: {str(e)}")

    def delete_department(self, department_id):
        confirm = messagebox.askyesno(self.parent.il8n.confirm_deletion, self.parent.il8n.are_you_sure_delete_department)
        if confirm:
            try:
                self.db.delete_department(department_id)
                messagebox.showinfo(self.parent.il8n.success, self.parent.il8n.department_deleted_successfully)
                self.show_departments()
            except Exception as e:
                messagebox.showerror(self.parent.il8n.error, f"{self.parent.il8n.failed_delete_department}: {str(e)}")





class DepartmentManagementWindow(customtkinter.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.il8n = languagepack.I18N(language='en')
        self.title(self.il8n.department_management)
        self.geometry("600x500")
        self.parent = parent
        self.db = StudentInfoSystem()

        self.create_widgets()

    def create_widgets(self):
        # Add Department Entry
        self.add_department_label = customtkinter.CTkLabel(self, text=self.il8n.add_department)
        self.add_department_label.pack(pady=10)
        self.department_name_entry = customtkinter.CTkEntry(self)
        self.department_name_entry.pack(pady=10)

        # Add Department Button
        self.add_department_button = customtkinter.CTkButton(self, text=self.il8n.add_department, command=self.add_department)
        self.add_department_button.pack(pady=10)

        # Show Departments Button
        self.show_departments_button = customtkinter.CTkButton(self, text=self.il8n.show_departments, command=self.show_departments)
        self.show_departments_button.pack(pady=10)

        # ... (Add other widgets as needed)

    def add_department(self):
        department_name = self.department_name_entry.get()

        if not department_name:
            msg.CTkMessagebox(title=self.il8n.error, message=self.il8n.enter_required_fields, icon="cancel")
            return

        try:
            # Add department to the database
            self.db.add_department(department_name)
            msg.CTkMessagebox(title=self.il8n.success, message=self.il8n.department_added_success, icon="check", option_1=self.il8n.thanks)
        except Exception as e:
            msg.CTkMessagebox(title=self.il8n.error, message=f"{self.il8n.failed_add_department}: {str(e)}", icon="cancel")

    def show_departments(self):
        # Retrieve and display the list of departments in a new window
        department_list_window = DepartmentListWindow(self, self.db)
        department_list_window.show_departments()