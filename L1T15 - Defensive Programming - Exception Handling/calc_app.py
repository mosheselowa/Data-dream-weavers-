import os  #Imports the os module for interacting with the operating systems

def calculate(num1, num2, operator):
    try:
        if operator == '+':
            return num1 + num2 #Returns the sum of num1 and num2
        elif operator == '-':
            return num1 - num2 #Returns the difference of num1 and num2
        elif operator == '*':
            return num1 * num2 #Returns the product of num1 and num2
        elif operator == '/':
            if num2 == 0:
                return "Not mathematically possible to divide by zero" #Returns an error message if num2 is zero
            return num1 / num2 #Returns the quotient of num1 and num2
        else:
            return "Cannot proceed due to an invalid operator entered" #Returns an error message if the operator is invalid
    except Exception as e:
        return f"An error has occurred during the calculation: {e}" #Returns an error message if any exception occurs

def record_equation(equation):
    try:
        with open("equations.txt", "a") as file: #Opens the file in append mode
            file.write(equation + "\n") #Writes the equation to the file
    except Exception as e:
        print(f"An error occurred while recording the equation: {e}") #Prints out an error message if any exception occurs

def print_previous_equations():
    try:
        with open("equations.txt", "r") as file: #Opens the file in read mode
            for line in file: #Iterates over each line in the file
                print(line.strip()) #Prints the line after removing leading/trailing whitespace
    except FileNotFoundError:
        print("No previous equations found.")
    except Exception as e:
        print(f"An error occurred while reading the equations file: {e}")

while True: #Main program loop
    print("\nCalculator Menu:")
    print("1. Perform Calculation")
    print("2. Print Previous Equations")
    print("3. Exit")

    choice = input("Enter your choice from the options given above: ")

    if choice == "1":
        try:
            num1 = float(input("Enter the first number of the equation: ")) #Prompt the user to enter the first number of their equation
            operator = input("Enter the operator you would like to use (+, -, *, /): ") #Prompt the user to enter the operation they want to use
            num2 = float(input("Enter the second number of the equation: ")) #Prompt the user to enter the second number of the equation

            result = calculate(num1, num2, operator) #Calls the clculator function
            print("Result:", result) #Print out the results of the equation

            equation = f"{num1} {operator} {num2} = {result}"
            record_equation(equation) #Calls the record_equation function

        except ValueError:
            print("You have entered an invalid input, please enter numbers only.")
        except Exception as e:
            print(f"An unexpected error has occurred: {e}")

    elif choice == "2":
        print_previous_equations()

    elif choice == "3":
        break #Exits the loop,ending the program

    else:
        print("Invalid choice, kindly try again.")
