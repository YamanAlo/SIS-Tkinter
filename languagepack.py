import glob

class I18N:
    def __init__(self, language, load_from_file=True):
        if load_from_file:
            if language in self.get_available_languages():
                self.load_data_from_file(language)
            else:
                raise NotImplementedError("Unsupported language. Add missing language file.")
        else:
            self.load_data(language)

    def load_data(self, language):
        if language == "en":
            self.load_data_in_english()
        elif language == "tr":
            self.load_data_in_turkish()
        elif language == 'ar':
            self.load_data_in_arabic()
        else:
            raise NotImplementedError("Unsupported language.")
        
    def set_language(self, language):
        self.language = language
        self.load_data(language)

    def load_data_in_english(self):
        return
    
    def load_data_in_turkish(self):
        return
    
    def load_data_in_arabic(self):
        return
    
    def load_data_from_file(self, language):
        language_data = {}
        language_file = f'data_{language}.lng'
        with open(language_file, encoding='utf-8') as f:
            for line in f:
                key, value = line.strip().split('=')
                language_data[key] = value
        
       
        self.student_id = language_data['student_id']
        self.first_name = language_data['first_name']
        self.last_name = language_data['last_name']
        self.email = language_data['email']
        self.phone = language_data['phone']
        self.address = language_data['address']
        self.city = language_data['city']
        self.add_student = language_data['add_student']
        self.update_student = language_data['update_student']
        self.delete_student = language_data['delete_student']
        self.student_management = language_data['student_management']
        self.course_name = language_data['course_name']
        self.course_code = language_data['course_code']
        self.add_course = language_data['add_course']
        self.update_course = language_data['update_course']
        self.delete_course = language_data['delete_course']
        self.course_management = language_data['course_management']
        self.language = language_data['language']
        self.apply_changes = language_data['apply_changes']
        self.create_database = language_data['create_database']
        self.clear_database = language_data['clear_database']
        self.settings = language_data['settings']
        self.dashboard = language_data['dashboard']
        self.show_list = language_data['show_list']
        self.edit = language_data['edit']
        self.delete = language_data['delete']
        self.edit_student = language_data['edit_student']
        self.save_changes = language_data['save_changes']
        self.error = language_data['error']
        self.required_fields = language_data['required_fields']
        self.no_numbers_allowed = language_data['no_numbers_allowed']
        self.student_id_number = language_data['student_id_number']
        self.phone_number = language_data['phone_number']
        self.first_name_alpha = language_data['first_name_alpha']
        self.last_name_alpha = language_data['last_name_alpha']
        self.email_format = language_data['email_format']
        self.success = language_data['success']
        self.student_updated = language_data['student_updated']
        self.failed_update_student = language_data['failed_update_student']
        self.confirm_deletion = language_data['confirm_deletion']
        self.confirm_delete_student = language_data['confirm_delete_student']
        self.failed_remove_student = language_data['failed_remove_student']
        self.student_added_success = language_data['student_added_success']
        self.failed_add_student = language_data['failed_add_student']
        self.edit_course = language_data['edit_course']
        self.enter_required_fields = language_data['enter_required_fields']
        self.no_numbers = language_data['no_numbers']
        self.course_added_success = language_data['course_added_success']
        self.failed_add_course = language_data['failed_add_course']
        self.are_you_sure_delete_course = language_data['are_you_sure_delete_course']
        self.course_deleted_successfully = language_data['course_deleted_successfully']
        self.failed_delete_course = language_data['failed_delete_course']
        self.course_list = language_data['course_list']
        self.english = language_data['english']
        self.turkish = language_data['turkish']
        self.arabic = language_data['arabic']
        self.thanks = language_data['thanks']
        self.language_set_to  = language_data['language_set_to']
        self.course_id = language_data['course_id']
        self.gender = language_data['gender']
        self.male = language_data['male']
        self.female = language_data['female']
        self.no_spaces_allowed = language_data['no_spaces_allowed']
        self.database_created = language_data['database_created']
        self.failed_create_database = language_data['failed_create_database']
        self.failed_clear_database = language_data['failed_clear_database']
        self.database_cleared = language_data['database_cleared']
        self.database_info = language_data['database_info']
        self.department_list = language_data['department_list']
        self.department_id = language_data['department_id']
        self.department_name = language_data['department_name']
        self.edit_department = language_data['edit_department']
        self.department_updated_successfully = language_data['department_updated_successfully']
        self.failed_update_department = language_data['failed_update_department']
        self.are_you_sure_delete_department = language_data['are_you_sure_delete_department']
        self.department_deleted_successfully = language_data['department_deleted_successfully']
        self.failed_delete_department = language_data['failed_delete_department']
        self.department_management = language_data['department_management']
        self.add_department = language_data['add_department']
        self.show_departments = language_data['show_departments'] 
        self.department_added_success = language_data['department_added_success']
        self.failed_add_department = language_data['failed_add_department']
        self.yes = language_data['yes']
        self.no = language_data['no']
        self.edit_student_id = language_data['edit_student_id']
        self.select_student_id = language_data['select_student_id']
        self.course_updated_success = language_data['course_updated_success']   
        self.Switch_Theme = language_data['Switch_Theme']
        self.show_list_title = language_data['show_list_title']
        self.edit_student_title = language_data['edit_student_title']
        self.edit_course_title = language_data['edit_course_title']
        self.edit_department_title = language_data['edit_department_title']
        self.failed_update_course = language_data['failed_update_course']
        self.already_exists = language_data['already_exists']
        self.department_already_exists = language_data['department_already_exists']
        self.course_name_already_exists = language_data['course_name_already_exists']
        self.code_already_exists = language_data['code_already_exists']
        self.name_code_already_exists = language_data['name_code_already_exists']
        self.department_already_exists_for_student = language_data['department_already_exists_for_student']
        self.deleted_student_success = language_data['deleted_student_success']
        
    @staticmethod
    def get_available_languages():
        language_files = glob.glob("*.lng")
        languages_codes = []

        for f in language_files:
            languages_code = f.replace('data_', '').replace('.lng', '')
            languages_codes.append(languages_code)
        
        return languages_codes