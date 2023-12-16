import sqlite3 

class StudentInfoSystem:

    def __init__(self):
        self.conn = None
        self.cursor = None

    @staticmethod

    def connect():
        return sqlite3.connect('StudentInfoSystem.db')

   
    def create_database(self):
        self.conn = self.connect()
        self.cursor = self.conn.cursor()
        query = '''CREATE TABLE IF NOT EXISTS student (
            student_id INTEGER PRIMARY KEY NOT NULL ,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email TEXT NOT NULL,
            phone int NOT NULL,
            address TEXT ,
            city TEXT )'''
        self.cursor.execute(query)

        query = '''CREATE TABLE IF NOT EXISTS courses (
            course_id INTEGER PRIMARY KEY NOT NULL ,
            course_name TEXT NOT NULL,
            course_code TEXT NOT NULL,
            course_description TEXT)'''
        self.cursor.execute(query)

        query = '''CREATE TABLE IF NOT EXISTS enrollment (
            student_id INTEGER NOT NULL,
            course_id INTEGER NOT NULL,
            FOREIGN KEY (student_id) REFERENCES student (student_id),
            FOREIGN KEY (course_id) REFERENCES courses (course_id))'''
        self.cursor.execute(query)
    
        # commit the changes
        self.conn.commit()
        self.conn.close()

    def add_student(self,student_id, first_name, last_name, email, phone, address, city):
        self.conn = self.connect()
        self.cursor = self.conn.cursor()
        self.cursor.execute("INSERT INTO student VALUES (NULL,?, ?, ?, ?, ?, ?, ?)", (student_id,first_name, last_name, email, phone, address or None, city or None))
        self.conn.commit()
        self.conn.close()

    def add_course(self, course_name, course_code, course_description):
        self.conn = self.connect()
        self.cursor = self.conn.cursor()
        self.cursor.execute("INSERT INTO courses VALUES (NULL, ?, ?, ?)", (course_name, course_code, course_description))
        self.conn.commit()
        self.conn.close()

    def add_enrollment(self, student_id, course_id):
        self.conn = self.connect()
        self.cursor = self.conn.cursor()
        self.cursor.execute("INSERT INTO enrollment VALUES (?, ?)", (student_id, course_id))
        self.conn.commit()
        self.conn.close()

    def get_students(self):
        self.conn = self.connect()
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM student")
        rows = self.cursor.fetchall()
        self.conn.close()
        return rows
    
    def get_courses(self):
        self.conn = self.connect()
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM courses")
        rows = self.cursor.fetchall()
        self.conn.close()
        return rows

    def get_enrollment(self):
        self.conn = self.connect()
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM enrollment")
        rows = self.cursor.fetchall()
        self.conn.close()
        return rows

    def delete_student(self, student_id):
        self.conn = self.connect()
        self.cursor = self.conn.cursor()
        self.cursor.execute("DELETE FROM student WHERE student_id=?", (student_id,))
        self.conn.commit()
        self.conn.close()

    def delete_course(self, course_id):
        self.conn = self.connect()
        self.cursor = self.conn.cursor()
        self.cursor.execute("DELETE FROM courses WHERE course_id=?", (course_id,))
        self.conn.commit()
        self.conn.close()
    
    def delete_enrollment(self, student_id, course_id):
        self.conn = self.connect()
        self.cursor = self.conn.cursor()
        self.cursor.execute("DELETE FROM enrollment WHERE student_id=? AND course_id=?", (student_id, course_id))
        self.conn.commit()
        self.conn.close()

    def update_student(self, student_id, first_name, last_name, email, phone, address, city):
        self.conn = self.connect()
        self.cursor = self.conn.cursor()
        self.cursor.execute("UPDATE student SET first_name=?, last_name=?, email=?, phone=?, address=?, city=? WHERE student_id=?", (first_name, last_name, email, phone, address, city, student_id))
        self.conn.commit()
        self.conn.close()

    def update_course(self, course_id, course_name, course_code, course_description):
        self.conn = self.connect()
        self.cursor = self.conn.cursor()
        self.cursor.execute("UPDATE courses SET course_name=?, course_code=?, course_description=? WHERE course_id=?", (course_name, course_code, course_description, course_id))
        self.conn.commit()
        self.conn.close()

    def update_enrollment(self, student_id, course_id):
        self.conn = self.connect()
        self.cursor = self.conn.cursor()
        self.cursor.execute("UPDATE enrollment SET student_id=?, course_id=? WHERE student_id=? AND course_id=?", (student_id, course_id, student_id, course_id))
        self.conn.commit()
        self.conn.close()
    
    def __del__(self):
        self.conn.close()
    