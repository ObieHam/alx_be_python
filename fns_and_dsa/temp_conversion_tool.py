FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def temp_conv():
    """Temperature Conversion Tool."""
    temperature = float(input("Enter the temperature to convert: "))
    temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if temperature_type == "F":
        print(f"{temperature}°F is equivalent to {convert_to_celsius(temperature):.2f}°C.")
    elif temperature_type == "C":
        print(f"{temperature}°C is equivalent to {convert_to_fahrenheit(temperature):.2f}°F.")
    else:
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# Run the conversion tool
temp_conv()
