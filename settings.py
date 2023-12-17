# settings.py

import customtkinter
from tkinter import messagebox
import languagepack
import CTkMessagebox as msg

# can you use it to change the language of the windows?
class SettingsWindow(customtkinter.CTkToplevel):
    def __init__(self, dashboard_window):
        super().__init__()
        self.title("Settings")
        self.geometry("400x300")
        self.dashboard_window = dashboard_window

        # Dropdown or other widgets for settings like language
        self.language_selector = customtkinter.CTkComboBox(self, values=["English", "Arabic", "Turkish"])
        self.language_selector.pack(pady=10)

        # Button to apply settings
        self.apply_button = customtkinter.CTkButton(self, text="Apply Changes", command=self.apply_changes)
        self.apply_button.pack(pady=20)

    def apply_changes(self):
            language = self.language_selector.get()
            if language == "English":
                language = "en"
            elif language == "Turkish":
                language = "tr"
            elif language == "Arabic":
                language = "ar"
            else:
                language = "en"

            self.dashboard_window.update_language(language)
            

            msg.CTkMessagebox(title = "Settings", message= f"Language set to {language}", icon = "check", option_1 = "Thanks")