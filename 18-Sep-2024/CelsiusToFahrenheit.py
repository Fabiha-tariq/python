# Celsius To Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Fahrenheit To Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Input for Celsius to Fahrenheit
celsius = int(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(celsius, "°C is equal to", fahrenheit, "°F.")

# Check if the user wants to convert Fahrenheit to Celsius
check = input("Want to check temperature in Fahrenheit (y/n): ")

if check == "y":
    fahrenheit = int(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(fahrenheit, "°F is equal to", celsius, "°C.")

elif check == "n":
    print("OK, NO ISSUE :)")

else:
    print("OK, THANKS! BYE BYE 👋🏻👋🏻👋🏻")
