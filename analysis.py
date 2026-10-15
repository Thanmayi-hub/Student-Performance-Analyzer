def student_analysis(student):
    print("\n========== PERFORMANCE ANALYSIS ==========")

    print("Roll Number :", student.roll_no)
    print("Name        :", student.name)
    print("Branch      :", student.branch)
    print("Year        :", student.year)

    print("------------------------------------------")

    print("Total Marks :", student.total_marks())
    print("Average     :", round(student.average_marks(), 2))
    print("Percentage  :", round(student.percentage(), 2), "%")
    print("Grade       :", student.grade())
    print("Attendance  :", student.attendance, "%")

    print("------------------------------------------")

    print("Status      :", student.performance_status())

    if student.marks:
        highest_subject = max(
            student.marks,
            key=student.marks.get
        )

        lowest_subject = min(
            student.marks,
            key=student.marks.get
        )

        print(
            "Best Subject:",
            highest_subject,
            "-",
            student.marks[highest_subject]
        )

        print(
            "Weak Subject:",
            lowest_subject,
            "-",
            student.marks[lowest_subject]
        )

    print("==========================================")
def class_statistics(students):

    if not students:
        print("No students available.")
        return

    percentages = [
        student.percentage()
        for student in students.values()
        if student.marks
    ]

    if not percentages:
        print("No marks available.")
        return

    print("\n========== CLASS STATISTICS ==========")

    print(
        "Class Average:",
        round(sum(percentages) / len(percentages), 2),
        "%"
    )

    print(
        "Highest Percentage:",
        round(max(percentages), 2),
        "%"
    )

    print(
        "Lowest Percentage:",
        round(min(percentages), 2),
        "%"
    )

    excellent = sum(
        1
        for student in students.values()
        if student.performance_status() == "Excellent"
    )

    at_risk = sum(
        1
        for student in students.values()
        if student.performance_status() == "At Risk"
    )

    print("Excellent Students:", excellent)
    print("At Risk Students:", at_risk)

    print("======================================")