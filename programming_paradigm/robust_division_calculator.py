def safe_divide(numerator, denominator):
    try:
        float(numerator)/float(denominator)
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    else:
        result = float(numerator)/float(denominator)
        print(f"The result of the division is {result}")
