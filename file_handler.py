# Reading and Writing Files
import csv
import json
from student import Student

# REad TXT file and Write
def read_txt(file_path):
    students = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if not line:
                continue
            parts = [p.strip() for p in line.split(',')]
            if len(parts) >= 7:
                s_id, name, dept, sem = parts[0], parts[1], parts[2], parts[3]
                marks = [int(x) for x in parts[4:7]]
                students.append(Student(s_id, name, dept, sem, marks))
    return students

def write_txt(file_path, students):
    with open(file_path, 'w') as f:
        for s in students:
            m_str = ", ".join(str(m) for m in s.marks)
            f.write(f"{s.student_id}, {s.name}, {s.department}, {s.semester}, {m_str}\n")

# Read CSV file and Write
def read_csv(file_path):
    students = []
    with open(file_path, 'r', newline='') as f:
        reader = csv.reader(f)
        header = next(reader, None)  # Skip first title row
        for row in reader:
            if row:
                s_id, name, dept, sem = row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip()
                marks = [int(x.strip()) for x in row[4:7]]
                students.append(Student(s_id, name, dept, sem, marks))
    return students

def write_csv(file_path, students):
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Student ID", "Name", "Department", "Semester", "Subject1", "Subject2", "Subject3"])
        for s in students:
            row = [s.student_id, s.name, s.department, s.semester] + s.marks
            writer.writerow(row)

# Read JSON file and Write
def read_json(file_path):
    students = []
    with open(file_path, 'r') as f:
        data = json.load(f)
        for item in data:
            s_id = item["student_id"]
            name = item["name"]
            dept = item["department"]
            sem = item["semester"]
            m_dict = item["marks"]
            marks = [m_dict["subject1"], m_dict["subject2"], m_dict["subject3"]]
            students.append(Student(s_id, name, dept, sem, marks))
    return students

def write_json(file_path, students):
    data = []
    for s in students:
        data.append({
            "student_id": int(s.student_id) if s.student_id.isdigit() else s.student_id,
            "name": s.name,
            "department": s.department,
            "semester": s.semester,
            "marks": {
                "subject1": s.marks[0] if len(s.marks) > 0 else 0,
                "subject2": s.marks[1] if len(s.marks) > 1 else 0,
                "subject3": s.marks[2] if len(s.marks) > 2 else 0
            }
        })
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)