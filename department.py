import customtkinter
from tkinter import messagebox, simpledialog, Menu
from tkinter import ttk
from database import StudentInfoSystem
import CTkMessagebox as msg
import languagepack
from CTkXYFrame import CTkXYFrame
import customtkinter
from tkinter import messagebox, Menu

class DepartmentListWindow(customtkinter.CTkToplevel):
    def __init__(self, parent, db):
        super().__init__(parent)
        self.il8n = languagepack.I18N(language='tr')
        self.title(self.il8n.department_list)
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
            edit_window.title(self.il8n.edit_department)
            edit_window.geometry("750x200")

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


            save_button = customtkinter.CTkButton(edit_window, text=self.il8n.save_changes,
                                        command=lambda: (lambda: self.save_changes(edit_window, department_id,
                                        new_dept_entry.get(), new_student_id_combobox.get())))
            
            save_button.pack(pady=10)

    def save_changes(self, edit_window, department_id, new_name, new_student_id):
        if not new_name or not new_student_id :
            msg.CTkMessagebox(title=self.il8n.error, message=self.il8n.enter_required_fields, icon="cancel")
            return

        try:
            self.db.update_department(department_id, new_name, new_student_id)
            msg.CTkMessagebox(title=self.il8n.success, message=self.il8n.department_updated_successfully, icon="check", option_1=self.il8n.thanks)
            self.show_departments()
            edit_window.destroy()
        except Exception as e:
           msg.CTkMessagebox(title=self.il8n.error, message=f"{self.il8n.failed_update_department}: {str(e)}, icon='cancel'")

    def delete_department(self, department_id):
        confirm = messagebox.askyesno(self.il8n.confirm_deletion, self.il8n.are_you_sure_delete_department)
        if confirm:
            try:
                self.db.delete_department(department_id)
                messagebox.showinfo(self.il8n.success, self.il8n.department_deleted_successfully)                
                self.show_departments()
                
            except Exception as e:
               messagebox.showerror(self.il8n.error, f"{self.il8n.failed_delete_department}: {str(e)}, icon='cancel'")





class DepartmentManagementWindow(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.il8n = languagepack.I18N(language='tr')
        self.title(self.il8n.department_management)
        self.geometry("600x500")
        
        self.db = StudentInfoSystem()

        self.create_widgets()

    def create_widgets(self):
        # Add Department Entry

        # student id 
        student_label = customtkinter.CTkLabel(self, text=self.il8n.student_id )
        student_label.pack(pady=5)

        # Combobox for selecting student
        self.student_combobox = ttk.Combobox(self)
        self.student_combobox.set(self.il8n.select_student_id)
        self.student_combobox.pack(pady=5)
        self.populate_student_combobox()
    

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
    
    def populate_student_combobox(self):
        students = self.db.get_students()
        student_ids = [str(student[0]) for student in students]
        self.student_combobox['values'] = ["Select Student ID"] + student_ids

    def add_department(self):
        department_name = self.department_name_entry.get()
        student_id = self.student_combobox.get()

        if not department_name or not student_id:
            msg.CTkMessagebox(title=self.il8n.error, message=self.il8n.enter_required_fields, icon="cancel")
            return
        
        if any(char.isdigit() for char in department_name):
            msg.CTkMessagebox(title=self.il8n.error, message=f"{self.il8n.department_name}{self.il8n.no_numbers}", icon="cancel")
            return
        
        # no spaces in student id 
        if any(char.isspace() for char in student_id):
            error_fields = [field for field, value in {"Student ID": student_id}.items() if any(char.isspace() for char in value)]
            error_message = f"{', '.join(error_fields)} {self.il8n.no_spaces_allowed}"
            msg.CTkMessagebox(title=self.il8n.error, message=error_message, icon="cancel")
            return
        
        


        try:
            # Add department to the database
            self.db.add_department(department_name, student_id)
            msg.CTkMessagebox(title=self.il8n.success, message=self.il8n.department_added_success, icon="check", option_1=self.il8n.thanks)
        except Exception as e:
            msg.CTkMessagebox(title=self.il8n.error, message=f"{self.il8n.failed_add_department}: {str(e)}", icon="cancel")

    def show_departments(self):
        # Retrieve and display the list of departments in a new window
        department_list_window = DepartmentListWindow(self, self.db)
        department_list_window.show_departments()