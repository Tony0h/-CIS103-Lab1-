# ------------------------------------
# CIS 103: Introduction to Programming
# Lab 02: "Calculator Function"
# Instructor: Md Ali
# Student Name: Antonio Valenzuela
# Date: 08/31/2024
#-------------------------------------
# This project will demonstrate the use of a calculator using addition, subtraction, multiplication, and division.
# Choosing a number between 1 through 5 will start the calculations
# The following code brings two variables together to add
def add(x,y):
    return x + y
# The following code subtracts one variable to the next
def subtract(x,y):
    return x - y
# The following code multiplies the given variables together
def multiply(x,y):
    return x * y
# The following line of code divides
def divide(x,y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero!."
# The following code defines a main function, with it being the user interface
def main():

        while True:
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Division")
            print("5. Exit")
# Inputting a choice asks the user to choose between the 5 choices
            choice = input("Enter choice: ")
# Asking an if statement which in this case being 5, exits the user and displays a thank uou message
            if choice == '5':
                print("exiting, thank you!")
                break
# Float allows decimals to take into account
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
# if statements below give the proper action to take place when choosing a number
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} + {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} + {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} + {num2} = {divide(num1, num2)}")
            else:
                print("Invalid input")

if __name__ == "__main__":
        main()