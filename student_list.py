import tkinter as tk
import sqlite3
import CTkMessagebox as msg
import languagepack
import customtkinter as ctk
from tkinter import messagebox, Menu
from CTkXYFrame import CTkXYFrame


class StudentListWindow(ctk.CTkToplevel):
    def __init__(self, parent, db):
        super().__init__(parent)
        self.il8n = languagepack.I18N(language='tr')
        self.title(self.il8n.show_list)
        self.geometry("900x400")
        self.parent = parent
        self.db = db 

        self.students_list_frame = ctk.CTkFrame(self)
        self.students_list_frame.pack(pady=20)


    def show_students_list(self):
        for widget in self.students_list_frame.winfo_children():
            widget.destroy()

        students = self.db.get_students()
        for student in students:
            label_text = f"{self.il8n.student_id}: {student[0]}, {self.il8n.first_name}: {student[1]}, {self.il8n.last_name}: {student[2]}, {self.il8n.email}: {student[3]}, {self.il8n.phone}: {student[4]}, {self.il8n.address}: {student[5]}, {self.il8n.city}: {student[6]}"
            label = ctk.CTkLabel(self.students_list_frame, text=label_text)
            label.bind("<Button-3>", lambda event, id=student[0]: self.show_context_menu(event, id))
            label.pack()
            
            self.grab_set()
            

    def show_context_menu(self, event, student_id):
        context_menu = Menu(self, tearoff=0)
        context_menu.add_command(label=self.il8n.edit, command=lambda: self.edit_student(student_id))
        context_menu.add_command(label=self.il8n.delete, command=lambda: self.delete_student(student_id))
        context_menu.post(event.x_root, event.y_root)

    def edit_student(self, student_id):
        students_details = self.db.get_students()  
        selected_student = next((student for student in students_details if student[0] == student_id), None)

        if selected_student:
            self.selected_student_id = student_id

            edit_window = ctk.CTkToplevel(self)
            edit_window.title(self.il8n.edit_student)
            edit_window.geometry("800x301")
            edit_window.grab_set()

            entry_frame = CTkXYFrame(edit_window, width=750, height=200,
                                         scrollbar_fg_color="blue",
                                         scrollbar_button_color="blue",
                                         scrollbar_button_hover_color="cyan")
            entry_frame.pack(pady=10)

            horizontal_scrollbar = ctk.CTkScrollbar(entry_frame, orientation="horizontal",
                                                     command=entry_frame.xy_canvas.xview)
            horizontal_scrollbar.pack(side="bottom", fill="x")
            entry_frame.xy_canvas.configure(xscrollcommand=horizontal_scrollbar.set)

            
            # Student ID
            student_id_label = ctk.CTkLabel(entry_frame, text=f"{self.il8n.student_id}:")
            student_id_label.pack(side='left', padx=5)
            new_id_entry = ctk.CTkEntry(entry_frame)
            new_id_entry.insert(0, selected_student[0])  
            new_id_entry.pack(side='left', padx=5)

            # First Name
            first_name_label = ctk.CTkLabel(entry_frame, text=f"{self.il8n.first_name}:")
            first_name_label.pack(side='left', padx=5)
            new_first_name_entry = ctk.CTkEntry(entry_frame)
            new_first_name_entry.insert(0, selected_student[1])  
            new_first_name_entry.pack(side='left', padx=5)

            # Last Name
            last_name_label = ctk.CTkLabel(entry_frame, text=f"{self.il8n.last_name}:")
            last_name_label.pack(side='left', padx=5)
            new_last_name_entry = ctk.CTkEntry(entry_frame)
            new_last_name_entry.insert(0, selected_student[2])  
            new_last_name_entry.pack(side='left', padx=5)

            # Email
            student_email_label = ctk.CTkLabel(entry_frame, text=f"{self.il8n.email}:")
            student_email_label.pack(side='left', padx=5)
            new_email_entry = ctk.CTkEntry(entry_frame)
            new_email_entry.insert(0, selected_student[3])  
            new_email_entry.pack(side='left', padx=5)

            # Phone
            student_phone_label = ctk.CTkLabel(entry_frame, text=f"{self.il8n.phone}:")
            student_phone_label.pack(side='left', padx=5)
            new_phone_entry = ctk.CTkEntry(entry_frame)
            new_phone_entry.insert(0, selected_student[4])  
            new_phone_entry.pack(side='left', padx=5)

            # Address
            student_address_label = ctk.CTkLabel(entry_frame, text=f"{self.il8n.address}:")
            student_address_label.pack(side='left', padx=5)
            new_address_entry = ctk.CTkEntry(entry_frame)
            new_address_entry.insert(0, selected_student[5])  
            new_address_entry.pack(side='left', padx=5)

            # City
            student_city_label = ctk.CTkLabel(entry_frame, text=f"{self.il8n.city}:")
            student_city_label.pack(side='left', padx=5)
            new_city_entry = ctk.CTkEntry(entry_frame)
            new_city_entry.insert(0, selected_student[6])  
            new_city_entry.pack(side='left', padx=5)

            # Save Changes Button
            save_button = ctk.CTkButton(edit_window, text=self.il8n.save_changes,
                                                  command=lambda: self.save_changes(edit_window,
                                                                                      new_id_entry.get(),
                                                                                      new_first_name_entry.get(),
                                                                                      new_last_name_entry.get(),
                                                                                      new_email_entry.get(),
                                                                                      new_phone_entry.get(),
                                                                                      new_address_entry.get(),
                                                                                      new_city_entry.get()))
            save_button.pack(pady=10)
            
    def save_changes(self, edit_window, student_id, first_name, last_name, email, phone, address, city):
         
        if not student_id or not first_name or not last_name or not email or not phone or not address or not city:
            msg.CTkMessagebox(title=self.il8n.error, message=self.il8n.required_fields, icon="cancel")
            return
        
        

        # Validate (no numbers allowed)
        if any(char.isdigit() for char in first_name + last_name + email + address + city):
            error_fields = [field for field, value in {"First Name": first_name, "Last Name": last_name,  "Address": address, "City": city}.items() if any(char.isdigit() for char in value)]
            error_message = f"{', '.join(error_fields)} {self.il8n.no_numbers_allowed}"
            msg.CTkMessagebox(title=self.il8n.error, message=error_message , icon="cancel")
            return

        # Validate (no spaces allowed)

        if any(char.isspace() for char in student_id + first_name + last_name + email + phone + address + city):
            error_fields = [field for field, value in {"Student ID": student_id, "First Name": first_name, "Last Name": last_name, "Email": email, "Phone": phone, "Address": address, "City": city}.items() if any(char.isspace() for char in value)]
            error_message = f"{', '.join(error_fields)} {self.il8n.no_spaces_allowed}"
            msg.CTkMessagebox(title=self.il8n.error, message=error_message, icon="cancel")
            return
    

        if not student_id.isdigit():
            msg.CTkMessagebox(title=self.il8n.error, message=self.il8n.student_id_number, icon="cancel")
            return
        
        if not phone.isdigit():
            msg.CTkMessagebox(title=self.il8n.error, message=self.il8n.phone_number, icon="cancel")
            return

        if not first_name.isalpha():
            msg.CTkMessagebox(title=self.il8n.error, message=self.il8n.first_name_alpha, icon="cancel")
            return
        
        if not last_name.isalpha():
            msg.CTkMessagebox(title=self.il8n.error, message=self.il8n.last_name_alpha, icon="cancel")
            return
        
        if not all(char.isalnum() or char in ['@', '.'] for char in email):
            msg.CTkMessagebox(title=self.il8n.error, message=self.il8n.email_format, icon="cancel")
            return
        
        try:
            self.db.update_student(student_id, first_name, last_name, email, phone, address, city)
            msg.CTkMessagebox(title=self.il8n.success, message=self.il8n.student_updated, icon="check" , option_1=self.il8n.thanks)
            self.show_students_list()
            self.grab_release()
            edit_window.destroy()  
        except Exception as e:
            msg.CTkMessagebox(title=self.il8n.error, message=f"{self.il8n.failed_update_student}: {e}", icon="cancel")
        
        

    def delete_student(self, student_id):
        try:
            self.db.delete_student(student_id)
            messagebox.showinfo(title=self.il8n.confirm_deletion, message=self.il8n.confirm_delete_student)
            self.show_students_list()  
            self.grab_release()
        except Exception as e:
            msg.CTkMessagebox(title=self.il8n.error, message=f"{self.il8n.failed_remove_student}: {e}", icon="cancel")