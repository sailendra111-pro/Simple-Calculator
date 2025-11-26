print("**TEMPERATURE CONVERSION PROGRAM**")
unit = input("Enter the unit you want to convert from Celsius, Fahrenheit, Kelvin  (C/F/K): ")
temp = float(input("Enter the temperature value: "))
if unit== "C":
    # Convert Celsius to Fahrenheit 
    result = (temp * 9/5) + 32
    print(f"{round(result,2)} F")
    # Convert Celsius to Kelvin
    result = temp + 273.15
    print(f"{round(result,2)} K")
elif unit== "F":
    # Convert Fahrenheit to Celsius 
    result = (temp - 32) * 5/9
    print(f"{round(result,2)}C")
    # Convert Fahrenheit to Kelvin
    result = (temp - 32) *5/9 + 273.15
    print(f"{round(result,2)} K")
elif unit== "K":    
    # Convert Kelvin to Celsius 
    result = temp - 273.15
    print(f"{round(result,2)} C")
    # Convert Kelvin to Fahrenheit
    result = (temp - 273.15) * 9/5 + 32
    print(f"{round(result,2)} F")
else:
    print("Invalid unit")