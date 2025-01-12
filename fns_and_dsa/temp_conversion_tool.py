FAHRENHEIT_TO_CELSIUS_FACTOR=(5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR=(9/5)
def convert_to_celsius(fahrenheit):
    return (FAHRENHEIT_TO_CELSIUS_FACTOR * fahrenheit) - 32
def convert_to_fahrenheit(celsius):
    return (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32
def temp_conv():
    temperature = int(input("Enter the temperature to convert: "))
    temperature_type = input ("s this temperature in Celsius or Fahrenheit? (C/F): ")
    if temperature_type == "F":
        print (convert_to_celsius(temperature))
    elif temperature_type == "C":
        print (convert_to_fahrenheit(temperature))
    else:
        print ("Invalid input")
temp_conv()
