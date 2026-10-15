class Student:
    def __init__(self, roll_no, name, branch, year):
        self.roll_no = roll_no
        self.name = name
        self.branch = branch
        self.year = year
        self.marks = {}
        self.attendance = 0

    def add_marks(self, subject, mark):
        self.marks[subject] = mark

    def set_attendance(self, attendance):
        self.attendance = attendance

    def total_marks(self):
        return sum(self.marks.values())

    def average_marks(self):
        if not self.marks:
            return 0

        return self.total_marks() / len(self.marks)

    def percentage(self):
        if not self.marks:
            return 0

        return self.total_marks() / len(self.marks)

    def grade(self):
        percentage = self.percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def performance_status(self):
        percentage = self.percentage()

        if percentage >= 75 and self.attendance >= 75:
            return "Excellent"
        elif percentage >= 60 and self.attendance >= 75:
            return "Good"
        elif percentage >= 50:
            return "Needs Improvement"
        else:
            return "At Risk"

    def to_dict(self):
        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "branch": self.branch,
            "year": self.year,
            "marks": self.marks,
            "attendance": self.attendance
        }

    @staticmethod
    def from_dict(data):
        student = Student(
            data["roll_no"],
            data["name"],
            data["branch"],
            data["year"]
        )

        student.marks = data.get("marks", {})
        student.attendance = data.get("attendance", 0)

        return student