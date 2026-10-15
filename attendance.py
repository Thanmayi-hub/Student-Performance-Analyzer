from validation import get_attendance


def update_attendance(student):
    print("\n--- Attendance ---")

    attendance = get_attendance(
        "Enter attendance percentage: "
    )

    student.set_attendance(attendance)

    print("Attendance updated successfully.")


def display_attendance(student):
    print("\nAttendance:", student.attendance, "%")