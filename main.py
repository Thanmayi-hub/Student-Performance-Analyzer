from student import Student
from marks import add_student_marks, display_marks
from attendance import update_attendance
from analysis import student_analysis, class_statistics
from reports import generate_report
from storage import save_students, load_students

from validation import (
    get_non_empty_input,
    get_positive_integer
)


students = load_students(Student)


def add_student():

    print("\n========== ADD STUDENT ==========")

    roll_no = get_non_empty_input(
        "Enter roll number: "
    )

    if roll_no in students:
        print("Student already exists.")
        return

    name = get_non_empty_input(
        "Enter student name: "
    )

    branch = get_non_empty_input(
        "Enter branch: "
    )

    year = get_positive_integer(
        "Enter year: "
    )

    student = Student(
        roll_no,
        name,
        branch,
        year
    )

    students[roll_no] = student

    save_students(students)

    print("\nStudent added successfully.")


def search_student():

    roll_no = get_non_empty_input(
        "Enter roll number: "
    )

    student = students.get(roll_no)

    if student:
        print("\nStudent Found")
        print("Name:", student.name)
        print("Branch:", student.branch)
        print("Year:", student.year)
    else:
        print("Student not found.")


def list_students():

    if not students:
        print("\nNo students available.")
        return

    print("\n========== STUDENTS ==========")

    for student in students.values():

        print(
            f"{student.roll_no} | "
            f"{student.name} | "
            f"{student.branch} | "
            f"Year {student.year}"
        )


def select_student():

    roll_no = get_non_empty_input(
        "Enter roll number: "
    )

    student = students.get(roll_no)

    if not student:
        print("Student not found.")

    return student


def delete_student():

    student = select_student()

    if not student:
        return

    del students[student.roll_no]

    save_students(students)

    print("Student deleted successfully.")


def student_menu():

    student = select_student()

    if not student:
        return

    while True:

        print("\n========== STUDENT MENU ==========")

        print("1. Add Marks")
        print("2. View Marks")
        print("3. Update Attendance")
        print("4. Performance Analysis")
        print("5. Generate Report")
        print("6. Back")

        choice = input("Enter choice: ")

        if choice == "1":

            add_student_marks(student)
            save_students(students)

        elif choice == "2":

            display_marks(student)

        elif choice == "3":

            update_attendance(student)
            save_students(students)

        elif choice == "4":

            student_analysis(student)

        elif choice == "5":

            generate_report(student)

        elif choice == "6":

            break

        else:

            print("Invalid choice.")


def main():

    while True:

        print("\n")
        print("=" * 45)
        print("     STUDENT PERFORMANCE ANALYZER")
        print("=" * 45)

        print("1. Add Student")
        print("2. List Students")
        print("3. Search Student")
        print("4. Student Management")
        print("5. Class Statistics")
        print("6. Delete Student")
        print("7. Exit")

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":

            add_student()

        elif choice == "2":

            list_students()

        elif choice == "3":

            search_student()

        elif choice == "4":

            student_menu()

        elif choice == "5":

            class_statistics(students)

        elif choice == "6":

            delete_student()

        elif choice == "7":

            save_students(students)

            print(
                "\nThank you for using "
                "Student Performance Analyzer!"
            )

            break

        else:

            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()