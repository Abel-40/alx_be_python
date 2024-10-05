fahrenheit_to_celsius_factor = 5/9
celsius_to_fahrenheit_factor = 9/5
def convert_to_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * fahrenheit_to_celsius_factor
  return celsius

def convert_to_fahrenheit(celsius):
  fahrenheit = (celsius * celsius_to_fahrenheit_factor) + 32
  return fahrenheit

temperature = input("Enter the temperature to convert: ")
if temperature.isdigit():
  user_option = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

  if user_option == "F":
          celsius = convert_to_celsius(int(temperature))
          print(f"{temperature}°F is {celsius:.2f}°C")
  elif user_option == "C":
          fahrenheit = convert_to_fahrenheit(int(temperature))
          print(f"{temperature}°C is {fahrenheit:.2f}°F")
else:
  print("Invalid temperature. Please enter a valid numeric value.")
      
