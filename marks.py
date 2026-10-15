from validation import get_non_empty_input, get_mark


def add_student_marks(student):
    print("\n--- Add Marks ---")

    subject = get_non_empty_input("Enter subject name: ")
    mark = get_mark("Enter marks (0-100): ")

    student.add_marks(subject, mark)

    print("Marks added successfully.")


def display_marks(student):
    print("\n--- Marks ---")

    if not student.marks:
        print("No marks available.")
        return

    for subject, mark in student.marks.items():
        print(f"{subject}: {mark}")