# Student Information System (SIS)
A comprehensive Student Information System built with Python and CustomTkinter, featuring a modern GUI for managing students, courses, and departments with multi-language support.

## Features
* Student Management: Add, edit, delete, and view student information
* Course Management: Manage courses and assign them to students
* Department Management: Organize students by departments
* Multi-language Support: Available in English, Turkish, and Arabic
* Modern UI: Built with CustomTkinter for a sleek, modern interface
* Database Integration: SQLite database for data persistence
* Dark/Light Theme: Toggle between dark and light themes

## Screenshots
The application features a clean, modern interface with:

* Dashboard with quick access to all modules
* Student management with detailed forms
* Course and department management
* Multi-language interface
* Theme switching capability

## Installation
### Prerequisites
* Python 3.7 or higher
* pip (Python package installer)

### Setup Instructions
Clone the repository:

```bash
git clone <your-repository-url>
cd GUI-with-Tkinter-Python
```
Install dependencies:

```bash
pip install -r requirements.txt
```
Run the application:

```bash
python main.py
```

## Dependencies
The project uses the following main dependencies:

* `customtkinter`: Modern and customizable tkinter
* `CTkMessagebox`: Custom message boxes for CustomTkinter
* `CTkTable`: Table widget for CustomTkinter
* `CTkXYFrame`: Custom scrollable frame (included in project)

### About CTkXYFrame
This project includes a custom component `CTkXYFrame` which provides advanced scrollable frames for CustomTkinter. This component is:

* Author: Akash Bora (Akascape)
* License: MIT
* Homepage: https://github.com/Akascape/CTkXYFrame
* Version: 0.3

The `CTkXYFrame` component is included directly in the project under the `CTkXYFrame/` directory and provides:

* Bidirectional scrolling (X and Y axes)
* Dynamic scrollbar visibility
* Mouse wheel support
* Customizable scrollbar appearance

## Project Structure
```
├── main.py                 # Main application entry point
├── database.py            # Database operations and models
├── student.py             # Student management module
├── course.py              # Course management module
├── department.py          # Department management module
├── student_list.py        # Student listing functionality
├── course_list.py         # Course listing functionality
├── department_list.py     # Department listing functionality
├── settings.py            # Application settings
├── languagepack.py        # Multi-language support
├── data_en.lng           # English language pack
├── data_tr.lng           # Turkish language pack
├── data_ar.lng           # Arabic language pack
├── CTkXYFrame/           # Custom scrollable frame component
│   ├── __init__.py
│   └── ctk_xyframe.py
├── SIS.db                # SQLite database file
└── requirements.txt      # Python dependencies
```

## Usage
### First Run
* Launch the application by running `python main.py`
* Click "Create Database" to initialize the SQLite database
* Use the various management modules to add students, courses, and departments

### Managing Students
* Click "Student Management" to open the student module
* Add new students with their personal information
* Edit or delete existing students
* View student lists with filtering options

### Managing Courses
* Access "Course Management" to handle course operations
* Create courses and assign them to students
* Edit course details and manage enrollments

### Managing Departments
* Use "Department Management" for organizational structure
* Create departments and assign students
* Manage departmental information

### Language Support
* Access Settings to change the interface language
* Supported languages: English, Turkish, Arabic
* Language changes apply immediately to the interface

### Theme Switching
* Use the theme switch on the main dashboard
* Toggle between dark and light modes
* Theme preference is applied across all windows

## Database Schema
The application uses SQLite with the following main tables:

* `student`: Student personal information
* `courses`: Course details and student assignments
* `department`: Department information and student assignments

## Acknowledgments
* CustomTkinter: For the modern GUI framework
* Akascape: For the CTkXYFrame scrollable component
* CTkMessagebox & CTkTable: For additional UI components

## Troubleshooting
### Common Issues
* Module not found errors: Ensure all dependencies are installed using `pip install -r requirements.txt`
* Database errors: Make sure to create the database using the "Create Database" button on first run
* Display issues: Try switching themes or restarting the application 
