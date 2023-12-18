import sqlite3

class StudentInfoSystem:
    def __init__(self):
        self.conn = None
        self.cursor = None

    @staticmethod
    def connect():
        return sqlite3.connect('StudentInfoSystem.db')

    def __enter__(self):
        self.conn = self.connect()
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.commit()
            self.conn.close()


   
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

        query = '''CREATE TABLE IF NOT EXISTS department (
            department_id INTEGER PRIMARY KEY NOT NULL,
            department_name TEXT NOT NULL,
            student_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES student (student_id))'''
        
        self.cursor.execute(query)
    
        # commit the changes
        self.conn.commit()
        self.conn.close()

    def clear_database(self):
        '''Clears all data from the database'''
        self.conn = self.connect()
        self.cursor = self.conn.cursor()
        query = '''DELETE FROM student'''
        self.cursor.execute(query)
        query = '''DELETE FROM courses'''
        self.cursor.execute(query)
        query = '''DELETE FROM enrollment'''
        self.cursor.execute(query)
        self.conn.commit()
        self.conn.close()
        


    def add_student(self, student_id ,first_name, last_name, email, phone, address, city):
        self.conn = self.connect()
        self.cursor = self.conn.cursor()
        self.cursor.execute("INSERT INTO student VALUES (?, ?, ?, ?, ?, ?, ?)", (student_id ,first_name, last_name, email, phone, address or None, city or None))
        self.conn.commit()
        self.conn.close()


    def add_course(self, course_name, course_code, course_description):
        self.conn = self.connect()
        self.cursor = self.conn.cursor()
        self.cursor.execute("INSERT INTO courses VALUES (NULL, ?, ?, ?)", (course_name, course_code, course_description))
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


    def add_department(self, department_name , department_id):
        self.conn = self.connect()
        self.cursor = self.conn.cursor()
        self.cursor.execute("INSERT INTO department VALUES (NULL, ?, ?)", (department_name,department_id))
        self.conn.commit()
        self.conn.close()

    def delete_department(self, department_id):
        self.conn = self.connect()
        self.cursor = self.conn.cursor()
        self.cursor.execute("DELETE FROM department WHERE department_id=?", (department_id,))
        self.conn.commit()
        self.conn.close()

    def update_department(self, department_id,department_name):
        self.conn = self.connect()
        self.cursor = self.conn.cursor()
        self.cursor.execute("UPDATE department SET department_name=? WHERE department_id=?", (department_name, department_id))
        self.conn.commit()
        self.conn.close()

    def get_department(self):
        self.conn = self.connect()
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM department")
        rows = self.cursor.fetchall()
        self.conn.close()
        return rows

    
    def __del__(self):
        if self.conn is not None:
         self.conn.close()