import json
import os

DATA_FILE = "data/students.json"


def save_students(students):
    data = {}

    for roll_no, student in students.items():
        data[roll_no] = student.to_dict()

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def load_students(Student):
    if not os.path.exists(DATA_FILE):
        return {}

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        students = {}

        for roll_no, student_data in data.items():
            students[roll_no] = Student.from_dict(student_data)

        return students

    except (json.JSONDecodeError, KeyError):
        print("Warning: Data file is corrupted.")
        return {}