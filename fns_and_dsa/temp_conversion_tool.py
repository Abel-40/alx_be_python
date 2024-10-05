fahrenheit_to_celsius_factor = 5 / 9
celsius_to_fahrenheit_factor = 9 / 5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * fahrenheit_to_celsius_factor
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * celsius_to_fahrenheit_factor) + 32
    return fahrenheit

try:
    temperature = float(input("Enter the temperature to convert: "))  # Allow floats (decimals)
    user_option = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if user_option == "F":
        celsius = convert_to_celsius(temperature)
        print(f"{temperature}°F is {celsius}°C")
    elif user_option == "C":
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {fahrenheit}°F")
    else:
        print("Invalid option. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
except ValueError:
    print("Invalid temperature. Please enter a valid numeric value.")
