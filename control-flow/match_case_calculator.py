first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = first_number + second_number
        print(f"The result is {result}.")
    case "-":
        result = first_number - second_number
        print(f"The result is {result}.")
    case "*":
        result = first_number * second_number
        print(f"The result is {result}.")
    case "/":
        if second_number == 0:
            print("You cannot divide by zero!")
        else:
            result = first_number / second_number
            print(f"The result is {result}.")
    case _:
        print("Invalid operation.")
