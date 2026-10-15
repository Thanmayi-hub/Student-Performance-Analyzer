import os


def generate_report(student):

    # Create reports folder if it doesn't exist
    os.makedirs("reports", exist_ok=True)

    filename = f"reports/{student.roll_no}_report.txt"

    with open(filename, "w", encoding="utf-8") as file:

        file.write("STUDENT PERFORMANCE REPORT\n")
        file.write("=" * 40 + "\n")

        file.write(f"Roll Number : {student.roll_no}\n")
        file.write(f"Name        : {student.name}\n")
        file.write(f"Branch      : {student.branch}\n")
        file.write(f"Year        : {student.year}\n")

        file.write("\nMARKS\n")
        file.write("-" * 40 + "\n")

        if student.marks:
            for subject, mark in student.marks.items():
                file.write(f"{subject}: {mark}\n")
        else:
            file.write("No marks available.\n")

        file.write("\nRESULT\n")
        file.write("-" * 40 + "\n")

        file.write(
            f"Total Marks: {student.total_marks()}\n"
        )

        file.write(
            f"Average: {student.average_marks():.2f}\n"
        )

        file.write(
            f"Percentage: {student.percentage():.2f}%\n"
        )

        file.write(
            f"Grade: {student.grade()}\n"
        )

        file.write(
            f"Attendance: {student.attendance}%\n"
        )

        file.write(
            f"Status: {student.performance_status()}\n"
        )

    print("\nReport generated successfully!")
    print("File:", filename)