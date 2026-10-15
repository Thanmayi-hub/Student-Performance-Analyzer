def get_non_empty_input(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("Input cannot be empty.")


def get_positive_integer(message):
    while True:
        try:
            value = int(input(message))

            if value > 0:
                return value

            print("Enter a positive number.")

        except ValueError:
            print("Please enter a valid number.")


def get_mark(message):
    while True:
        try:
            mark = float(input(message))

            if 0 <= mark <= 100:
                return mark

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Enter a valid mark.")


def get_attendance(message):
    while True:
        try:
            attendance = float(input(message))

            if 0 <= attendance <= 100:
                return attendance

            print("Attendance must be between 0 and 100.")

        except ValueError:
            print("Enter a valid attendance percentage.")