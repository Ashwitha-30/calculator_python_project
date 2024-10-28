# Simple Calculator Program

# Function to perform basic operations
def calculate():
    print("Welcome to the Simple Calculator!")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Get the user's choice
    choice = input("Enter choice (1/2/3/4): ")

    # Get two numbers from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the selected operation
    if choice == '1':
        result = num1 + num2
        print(f"The result of addition: {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"The result of subtraction: {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"The result of multiplication: {result}")
    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result of division: {result}")
    else:
        print("Invalid choice. Please select a valid operation.")

# Call the calculate function
calculate()