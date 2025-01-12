def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num1 or num2 == 0:
            print("You can't divide by zero!")
        else:
            return num1/num2
    else:
        return "Input error!"