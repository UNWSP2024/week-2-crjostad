# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (9/5) * celsius + 32

# Ask the user to enter a temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert the temperature to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# Display the temperature in Fahrenheit
print(f"{celsius}°C is equal to {fahrenheit}°F")
