import os  # Imports the os module; not used in this snippet, but typically useful for file operations or OS-level tasks

# Function to perform basic arithmetic operations
def calculate(num1, num2, operator):
    try:
        # Check which operator is provided and perform corresponding operation
        if operator == '+':
            return num1 + num2  # Returns the sum of num1 and num2
        elif operator == '-':
            return num1 - num2  # Returns the difference of num1 and num2
        elif operator == '*':
            return num1 * num2  # Returns the product of num1 and num2
        elif operator == '/':
            if num2 == 0:
                return "Not mathematically possible to divide by zero"  # Handles division by zero error
            return num1 / num2  # Returns the result of division if num2 is not zero
        else:
            return "Cannot proceed due to an invalid operator entered"  # Handles case where operator is not recognized
    except Exception as e:
        # Catch-all for unexpected exceptions during calculation
        return f"An error has occurred during the calculation: {e}"

# Function to record a string representation of an equation to a file
def record_equation(equation):
    try:
        # Open (or create if not existing) 'equations.txt' in append mode
        with open("equations.txt", "a") as file:
            file.write(equation + "\n")  # Append the equation followed by a newline
    except Exception as e:
        # Print any exception that occurs while trying to write to the file
        print(f"An error occurred while recording the equation: {e}")

# Function to read and print previously recorded equations
def print_previous_equations():
    try:
        # Open 'equations.txt' in read mode
        with open("equations.txt", "r") as file:
            for line in file:
                print(line.strip())  # Print each line, removing any extra whitespace or newline characters
    except FileNotFoundError:
        # Handle the case when the file doesn't exist
        print("No previous equations found.")
    except Exception as e:
        # Catch-all for other unexpected file I/O errors
        print(f"An error occurred while reading the equations file: {e}")

# Main program loop that displays a menu and processes user input
while True:
    print("\nCalculator Menu:")
    print("1. Perform Calculation")
    print("2. Print Previous Equations")
    print("3. Exit")

    choice = input("Enter your choice from the options given above: ")  # Get user's menu selection

    if choice == "1":
        try:
            # Prompt user for numbers and operator
            num1 = float(input("Enter the first number of the equation: "))  # Convert user input to float
            operator = input("Enter the operator you would like to use (+, -, *, /): ")  # Get arithmetic operator
            num2 = float(input("Enter the second number of the equation: "))  # Convert second input to float

            result = calculate(num1, num2, operator)  # Perform calculation
            print("Result:", result)  # Display result to user

            # Format and save the equation and result
            equation = f"{num1} {operator} {num2} = {result}"
            record_equation(equation)  # Save the equation to file

        except ValueError:
            # Handles non-numeric input from the user
            print("You have entered an invalid input, please enter numbers only.")
        except Exception as e:
            # Handles any other unexpected errors during input or calculation
            print(f"An unexpected error has occurred: {e}")

    elif choice == "2":
        # If user selects to view previous calculations, call function
        print_previous_equations()

    elif choice == "3":
        # Exit the loop and end the program
        break

    else:
        # Handle any invalid menu input
        print("Invalid choice, kindly try again.")
