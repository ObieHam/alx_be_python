first_number = input("Enter the first number:")
second_number = input("Enter the second number:")
operation = input("Choose the operation (+, -, *, /):")
match operation:
    case "+":
        print ("The result is ", first_number + second_number, ".")
    case "-":
        print ("The result is ", first_number - second_number, ".")
    case "*":
        print ("The result is ", first_number * second_number, "."r)
    case "/":
        if second_number == 0:
            print("You cannot divide by zero!")
        else:
            print ("The result is ", first_number / second_number, ".")
