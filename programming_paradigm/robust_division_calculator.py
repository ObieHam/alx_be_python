def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)  # Perform division once
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    else:
        # Only print the result in the else block if division was successful
        print(f"The result of the division is {result}")
