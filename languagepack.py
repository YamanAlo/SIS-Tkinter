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
        self.student_id = "Student ID"
        self.first_name = "First Name"
        self.last_name = "Last Name"
        self.email = "Email"
        self.phone = "Phone"
        self.address = "Address"
        self.city = "City"
        self.add_student = "Add Student"
        self.update_student = "Update Student"
        self.delete_student = "Delete Student"
        self.student_management = "Student Management"
        self.course_name = "Course Name"
        self.course_code = "Course Code"
        self.add_course = "Add Course"
        self.update_course = "Update Course"
        self.delete_course = "Delete Course"
        self.course_management = "Course Management"
        self.enrollment_id = "Enrollment ID"
        self.enrollment_date = "Enrollment Date"
        self.add_enrollment = "Add Enrollment"
        self.update_enrollment = "Update Enrollment"
        self.delete_enrollment = "Delete Enrollment"
        self.enrollment_management = "Enrollment Management"
        self.language = "Language"
        self.apply_changes = "Apply Changes"
        self.create_database = "Create Database"
        self.clear_database = "Clear Database"
        self.settings = "Settings"
        self.dashboard = "Dashboard"
        self.show_list = "Show List"
        self.edit = "Edit"
        self.delete = "Delete"
        self.edit_student = "Edit Student"
        self.save_changes = "Save Changes"
        self.error = "Error"
        self.required_fields = "Please enter all required fields."
        self.no_numbers_allowed = 'should not contain numbers.'
        self.student_id_number = "Student ID should be a number."
        self.phone_number = "Phone number should be a number."
        self.first_name_alpha = "First Name should contain only alphabets."
        self.last_name_alpha = "Last Name should contain only alphabets."
        self.email_format = "Email should contain only alphabets, numbers, '@', and '.'"
        self.success = "Success"
        self.student_updated = "Student updated successfully."
        self.failed_update_student = "Failed to update student."
        self.confirm_deletion = "Confirm Deletion"
        self.confirm_delete_student = "Are you sure you want to delete this student?"
        self.failed_remove_student = "Failed to delete student."
        self.student_added_success = "Student added successfully."
        self.failed_add_student = "Failed to add student."
        self.edit_course = "Edit Course"
        self.enter_required_fields = "Please enter both Course Name and Course Code."
        self.no_numbers = "should not contain numbers."
        self.course_added_success = "Course added successfully."
        self.failed_add_course = "Failed to add course."
        self.are_you_sure_delete_course = "Are you sure you want to delete this course?"
        self.course_deleted_successfully = "Course deleted successfully."
        self.failed_delete_course = "Failed to delete course."
        self.course_list = 'Course List'
        self.english = 'English'
        self.turkish = 'Turkish'
        self.arabic = 'Arabic'
        self.thanks = 'Thanks'
        self.language_set_to  = 'Language set to'
        self.course_id = "Course ID"
        self.gender = 'Gender'
        self.male = 'Male'
        self.female = 'Female'
        self.no_spaces_allowed = 'should not contain spaces.'
        self.database_created = "Database created successfully."
        self.failed_create_database = "Failed to create database."
        self.failed_clear_database = "Failed to clear database."
        self.database_cleared = "Database cleared successfully."
        self.database_info = "Database Info"

        
    def load_data_in_turkish(self):
        self.student_id = "Öğrenci Numarası"
        self.first_name = "İsim"
        self.last_name = "Soyisim"
        self.email = "E-posta"
        self.phone = "Telefon"
        self.address = "Adres"
        self.city = "Şehir"
        self.add_student = "Öğrenci Ekle"
        self.update_student = "Öğrenci Güncelle"
        self.delete_student = "Öğrenci Sil"
        self.student_management = "Öğrenci Yönetimi"
        self.course_name = "Ders Adı"
        self.course_code = "Ders Kodu"
        self.add_course = "Ders Ekle"
        self.update_course = "Ders Güncelle"
        self.delete_course = "Ders Sil"
        self.course_management = "Ders Yönetimi"
        self.enrollment_id = "Kayıt Numarası"
        self.enrollment_date = "Kayıt Tarihi"
        self.add_enrollment = "Kayıt Ekle"
        self.update_enrollment = "Kayıt Güncelle"
        self.delete_enrollment = "Kayıt Sil"
        self.enrollment_management = "Kayıt Yönetimi"
        self.language = "Dil"
        self.apply_changes = "Değişiklikleri Uygula"
        self.create_database = "Veritabanı Oluştur"
        self.clear_database = "Veritabanını Temizle"
        self.settings = "Ayarlar"
        self.dashboard = "Kontrol Paneli"
        self.show_list = "Listeyi Göster"
        self.edit = "Düzenle"
        self.delete = "Sil"
        self.edit_student = "Öğrenci Düzenle"
        self.save_changes = "Değişiklikleri Kaydet"
        self.error = "Hata"
        self.required_fields = "Lütfen tüm gerekli alanları doldurun."
        self.no_numbers_allowed = 'sayı içermemelidir.'
        self.student_id_number = "Öğrenci Numarası bir sayı olmalıdır."
        self.phone_number = "Telefon numarası bir sayı olmalıdır."
        self.first_name_alpha = "İsim sadece harfler içermelidir."
        self.last_name_alpha = "Soyisim sadece harfler içermelidir."
        self.email_format = "E-posta sadece harfler, sayılar, '@' ve '.' içermelidir."
        self.success = "Başarılı"
        self.student_updated = "Öğrenci başarıyla güncellendi."
        self.failed_update_student = "Öğrenci güncellenemedi."
        self.confirm_deletion = "Silme Onayı"
        self.confirm_delete_student = "Bu öğrenciyi silmek istediğinizden emin misiniz?"
        self.failed_remove_student = "Öğrenci silinemedi."
        self.student_added_success = "Öğrenci başarıyla eklendi."
        self.failed_add_student = "Öğrenci eklenemedi."
        self.edit_course = "Ders Düzenle"
        self.enter_required_fields = "Lütfen Ders Adı ve Ders Kodu alanlarını doldurun."
        self.no_numbers = "sayı içermemelidir."
        self.course_added_success = "Ders başarıyla eklendi."
        self.failed_add_course = "Ders eklenemedi."
        self.are_you_sure_delete_course = "Bu dersi silmek istediğinizden emin misiniz?"
        self.course_deleted_successfully = "Ders başarıyla silindi."
        self.failed_delete_course = "Ders silinemedi."
        self.course_list = 'Ders Listesi'
        self.english = 'İngilizce'
        self.turkish = 'Türkçe'
        self.arabic = 'Arapça'
        self.thanks = 'Teşekkürler'
        self.language_set_to  = 'Dil ayarlandı'
        self.course_id = "Ders ID"
        self.gender = "Cinsiyet"
        self.male = "Erkek"
        self.female = "Kadın"
        self.no_spaces_allowed = 'boşluk içermemelidir.'
        self.database_created = "Veritabanı başarıyla oluşturuldu."
        self.failed_create_database = "Veritabanı oluşturulamadı."
        self.failed_clear_database = "Veritabanı temizlenemedi."
        self.database_cleared = "Veritabanı başarıyla temizlendi."
        self.database_info = "Veritabanı Bilgisi"



    def load_data_in_arabic(self):
        self.student_id = "رقم الطالب"
        self.first_name = "الاسم الاول"
        self.last_name = "الكنية"
        self.email = "البريد الإلكتروني"
        self.phone = "هاتف"
        self.address = "عنوان"
        self.city = "مدينة"
        self.add_student = "إضافة طالب"
        self.update_student = "تحديث الطالب"
        self.delete_student = "حذف الطالب"
        self.student_management = "إدارة الطلاب"
        self.course_name = "اسم الدورة"
        self.course_code = "رمز الدورة"
        self.add_course = "إضافة دورة"
        self.update_course = "تحديث الدورة"
        self.delete_course = "حذف الدورة"
        self.course_management = "إدارة الدورات"
        self.enrollment_id = "رقم التسجيل"
        self.enrollment_date = "تاريخ التسجيل"
        self.add_enrollment = "إضافة تسجيل"
        self.update_enrollment = "تحديث التسجيل"
        self.delete_enrollment = "حذف التسجيل"
        self.enrollment_management = "إدارة التسجيل"
        self.language = "لغة"
        self.apply_changes = "تطبيق التغييرات"
        self.create_database = "إنشاء قاعدة بيانات"
        self.clear_database = "مسح قاعدة البيانات"
        self.settings = "الإعدادات"
        self.dashboard = "لوحة القيادة"
        self.show_list = "إظهار القائمة"
        self.edit = "تعديل"
        self.delete = "حذف"
        self.edit_student = "تحرير الطالب"
        self.save_changes = "حفظ التغييرات"
        self.error = "خطأ"
        self.required_fields = "الرجاء إدخال جميع الحقول المطلوبة."
        self.no_numbers_allowed = 'يجب ألا يحتوي على أرقام.'
        self.student_id_number = "يجب أن يكون رقم الطالب رقمًا."
        self.phone_number = "يجب أن يكون رقم الهاتف رقمًا."
        self.first_name_alpha = "يجب أن يحتوي الاسم الأول على أحرف فقط."
        self.last_name_alpha = "يجب أن يحتوي الاسم الأخير على أحرف فقط."
        self.email_format = "يجب أن يحتوي البريد الإلكتروني على أحرف فقط وأرقام و '@' و '.'"
        self.success = "نجاح"
        self.student_updated = "تم تحديث الطالب بنجاح."
        self.failed_update_student = "فشل تحديث الطالب."
        self.confirm_deletion = "تأكيد الحذف"
        self.confirm_delete_student = "هل أنت متأكد أنك تريد حذف هذا الطالب؟"
        self.failed_remove_student = "فشل حذف الطالب."
        self.student_added_success = "تمت إضافة الطالب بنجاح."
        self.failed_add_student = "فشل إضافة الطالب."
        self.edit_course = "تحرير الدورة"
        self.enter_required_fields = "الرجاء إدخال كل من اسم الدورة ورمز الدورة."
        self.no_numbers = "يجب ألا يحتوي على أرقام."
        self.course_added_success = "تمت إضافة الدورة بنجاح."
        self.failed_add_course = "فشل إضافة الدورة."
        self.are_you_sure_delete_course = "هل أنت متأكد أنك تريد حذف هذه الدورة؟"
        self.course_deleted_successfully = "تم حذف الدورة بنجاح."
        self.failed_delete_course = "فشل حذف الدورة."
        self.course_list = 'قائمة الدورات'
        self.english = 'الإنجليزية'
        self.turkish = 'اللغة التركية'
        self.arabic = 'العربية'
        self.thanks = 'شكرا'
        self.language_set_to  = 'تم تعيين اللغة على'
        self.course_id = "معرف الدورة"
        self.gender = 'جنس'
        self.male = "ذكر"
        self.female= "أنثى"
        self.no_spaces_allowed = 'يجب ألا يحتوي على مسافات.'
        self.database_created = "تم إنشاء قاعدة البيانات بنجاح."
        self.failed_create_database = "فشل إنشاء قاعدة البيانات."
        self.failed_clear_database = "فشل مسح قاعدة البيانات."
        self.database_cleared = "تم مسح قاعدة البيانات بنجاح."
        self.database_info = "معلومات قاعدة البيانات"


    def load_data_from_file(self, language):
        language_data = {}
        language_file = f'data_{language}.lng'
        with open(language_file, encoding='utf-8') as f:
            for line in f:
                key, value = line.strip().split('=')
                language_data[key] = value
        
        # set the data
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
        self.enrollment_id = language_data['enrollment_id']
        self.enrollment_date = language_data['enrollment_date']
        self.add_enrollment = language_data['add_enrollment']
        self.update_enrollment = language_data['update_enrollment']
        self.delete_enrollment = language_data['delete_enrollment']
        self.enrollment_management = language_data['enrollment_management']
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

        
    @staticmethod
    def get_available_languages():
        language_files = glob.glob("*.lng")
        languages_codes = []

        for f in language_files:
            languages_code = f.replace('data_', '').replace('.lng', '')
            languages_codes.append(languages_code)
        
        return languages_codes