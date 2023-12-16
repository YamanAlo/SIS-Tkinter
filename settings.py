import customtkinter
import database

class SettingsWindow(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Settings")
        self.geometry("400x300")

        # Dropdown or other widgets for settings like language
        self.language_selector = customtkinter.CTkComboBox(self, values=["English", "Spanish", "French"])
        self.language_selector.pack(pady=10)

        # Button to apply settings
        self.apply_button = customtkinter.CTkButton(self, text="Apply Changes", command=self.apply_changes)
        self.apply_button.pack(pady=20)

    def apply_changes(self):
        language = self.language_selector.get()
        # Logic to apply changes, like setting the language
        print(f"Apply Changes: Language set to {language}")

# Opened from the Dashboard Window
