from add import add
#from subtract import subtract
#from multiply import multiply
#from divide import divide


def calculator():
    print("Select operation:")
    print("1: Addition (+)")
    print("2: Subtraction (-)")
    print("3: Multiplication (*)")
    print("4: Division (/)")

    
    try:
        choice = int(input("Enter the operation number (1, 2, 3, 4): "))
    except ValueError:
        print("Invalid input! Please enter a number corresponding to an operation.")
        return

    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
        return

    
    operations = {
        1: add,
        #2: subtract,
        #3: multiply,
        #4: divide
    }

    
    operation_function = operations.get(choice)

   
    if operation_function:
        result = operation_function(num1, num2)
        print(f"The result is: {result}")
    else:
        print("Invalid operation selected.")


if __name__ == "__main__":
    calculator()
