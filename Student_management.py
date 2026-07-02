import csv
from datetime import datetime

students = []


# Load Students From CSV
def load_students():
    try:
        with open("students.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) < 5:
                    continue

                student = {
                    "name": row[0],
                    "roll": row[1],
                    "class": row[2],
                    "marks": int(row[3]),
                    "date": row[4]
                }

                students.append(student)

    except FileNotFoundError:
        pass


# Save All Students
def save_all_students():
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)

        for s in students:
            writer.writerow([
                s["name"],
                s["roll"],
                s["class"],
                s["marks"],
                s["date"]
            ])


# Add Student
def add_student():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    student_class = input("Enter Class: ")

    try:
        marks = int(input("Enter Marks: "))
    except ValueError:
        print("Invalid Marks!")
        return

    now = datetime.now()

    student = {
        "name": name,
        "roll": roll,
        "class": student_class,
        "marks": marks,
        "date": now.strftime("%Y-%m-%d")
    }

    students.append(student)

    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            student["name"],
            student["roll"],
            student["class"],
            student["marks"],
            student["date"]
        ])

    print("Student Added Successfully!")


# View Students
def view_students():
    if len(students) == 0:
        print("No Students Found!")
        return

    print("\n===== Students List =====")

    for i, s in enumerate(students, start=1):
        print(
            i,
            "- Name:", s["name"],
            "- Roll:", s["roll"],
            "- Class:", s["class"],
            "- Marks:", s["marks"],
            "- Date:", s["date"]
        )


# Total Students
def total_students():
    print("Total Students =", len(students))


# Delete Student
def delete_student():
    if len(students) == 0:
        print("No Students Found!")
        return

    view_students()

    try:
        number = int(input("Enter Student Number To Delete: "))
    except ValueError:
        print("Invalid Number!")
        return

    if 1 <= number <= len(students):
        del students[number - 1]
        save_all_students()
        print("Student Deleted Successfully!")
    else:
        print("Invalid Student Number!")


# Edit Student
def edit_student():
    if len(students) == 0:
        print("No Students Found!")
        return

    view_students()

    try:
        number = int(input("Enter Student Number To Edit: "))
    except ValueError:
        print("Invalid Input!")
        return

    if 1 <= number <= len(students):

        name = input("Enter New Name: ")
        roll = input("Enter New Roll Number: ")
        student_class = input("Enter New Class: ")

        try:
            marks = int(input("Enter New Marks: "))
        except ValueError:
            print("Invalid Marks!")
            return

        now = datetime.now()

        students[number - 1]["name"] = name
        students[number - 1]["roll"] = roll
        students[number - 1]["class"] = student_class
        students[number - 1]["marks"] = marks
        students[number - 1]["date"] = now.strftime("%Y-%m-%d")

        save_all_students()

        print("Student Updated Successfully!")

    else:
        print("Invalid Student Number!")


# Program Start
load_students()


# Main Menu
while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Total Students")
    print("4. Delete Student")
    print("5. Edit Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        total_students()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        edit_student()

    elif choice == "6":
        print("Good Bye!")
        break

    else:
        print("Invalid Choice!")