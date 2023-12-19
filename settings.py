import customtkinter
from tkinter import messagebox
import languagepack
import CTkMessagebox as msg

class SettingsWindow(customtkinter.CTkToplevel):
    def __init__(self, dashboard_window):
        super().__init__()
        self.il8n = languagepack.I18N(language='en')
        self.title(self.il8n.settings)
        self.geometry("400x150")
        self.dashboard_window = dashboard_window
        
        
        language_options = [self.il8n.english, self.il8n.arabic, self.il8n.turkish]
        self.language_selector = customtkinter.CTkComboBox(self, values=language_options)
        self.language_selector.pack(pady=10)

        # Button to apply settings
        self.apply_button = customtkinter.CTkButton(self, text=self.il8n.apply_changes, command=self.apply_changes)
        self.apply_button.pack(pady=20)

    def apply_changes(self):
        language = self.language_selector.get()
        if language == self.il8n.english:
            language = "en"
        elif language == self.il8n.turkish:
            language = "tr"
        elif language == self.il8n.arabic:
            language = "ar"
        else:
            language = "en"

        self.dashboard_window.update_language(language)

        msg.CTkMessagebox(title=self.il8n.settings, message=f"{self.il8n.language_set_to} {language}", icon="check", option_1=self.il8n.thanks)
