#-----------------------------------------------
# CIS 103: Fundamentals to Programming
# Student Names: Antonio Valenzuela, Anthony Crespo, Brionne Warner
# Project: Student Grade Management System Lab
# Instructor: Md Ali
#Date: 09/27/24
#------------------------------------------------
# function that defines class average
def class_average():
    avg = student_grades
    if avg>= 90:
            print("A")
    elif avg>= 80:
            print("B")
    elif avg>= 70:
            print("C")
    elif avg>= 60:
            print("D")
    else:
            return "F"
# The main function that displays user interface
def main():
# While true function displaying four choices for the user
        while True:
            print("Student Grade Management System")
            print("1. Add a student")
            print("2. Add a grade")
            print("3. Show class average")
            print("4. Exit")


            choice = input("Enter choice: ")
# Empty lists made for student names and grades
            student_system = []
            student_grades = []
# Option that exits the user from the system
            if choice == '4':
                print("Exiting now...")
                break
# Inserts user name into the student system list while displaying a message
            if choice == '1':
                name = input("Enter student name: ")
                student_system.append(name)
                print(f"Student {name} was added")

            elif choice == '2':
                name = input("Enter student name: ")
                grade = float(input(f"Enter student grade: "))
                student_grades.append(grade)
                print(f" Grade {grade}, was added for {name}")
            elif choice == '3':
                print(class_average)
                return
#                return sum(student_system) / len(student_grades)
#                return

            else:
                print("Invalid input, pick a choice")


if __name__ == "__main__":
        main()



