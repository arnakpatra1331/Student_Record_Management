# Management of multiple student objects
from student import Student
import file_handler

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        updated = []
        for s in self.students:
            if s.student_id != str(student_id):
                updated.append(s)
        self.students = updated

    def display_all_students(self):
        if not self.students:
            print("No student records found !")
            return
        for s in self.students:
            s.display_student()

    def search_by_id(self, student_id):
        results = []
        for s in self.students:
            if s.student_id == str(student_id):
                results.append(s)
        return results

    def search_by_name(self, name):
        results = []
        for s in self.students:
            if name.lower() in s.name.lower():
                results.append(s)
        return results

    def search_by_department(self, dept):
        results = []
        for s in self.students:
            if dept.lower() in s.department.lower():
                results.append(s)
        return results

    def search_by_average(self, min_avg):
        results = []
        for s in self.students:
            if s.calculate_average() >= float(min_avg):
                results.append(s)
        return results

    def load_from_file(self, file_path, file_format):
        fmt = file_format.lower()
        if fmt == 'txt':
            self.students = file_handler.read_txt(file_path)
        elif fmt == 'csv':
            self.students = file_handler.read_csv(file_path)
        elif fmt == 'json':
            self.students = file_handler.read_json(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_format}")

    def save_to_file(self, file_path, file_format):
        fmt = file_format.lower()
        if fmt == 'txt':
            file_handler.write_txt(file_path, self.students)
        elif fmt == 'csv':
            file_handler.write_csv(file_path, self.students)
        elif fmt == 'json':
            file_handler.write_json(file_path, self.students)
        else:
            raise ValueError(f"Unsupported file format: {file_format}")