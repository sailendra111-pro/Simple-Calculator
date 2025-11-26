print("**CALCULATOR PROGRAM**")
unit= input("Enter the unit you want to convert from (kg, g, lb): ")
value = float(input("Enter the value you want to convert: "))
if unit == "kg":
    result = value * 2.20462      #kg to lb #1kg = 2.20462 lb
    print(f"{value} kg is equal to {round(result, 2)} lb")
    result = value * 1000         #kg to g   #1kg = 1000 g
    print(f"{value} kg is equal to {round(result, 2)} g") 
elif unit == "g":
    result = value / 1000         #g to kg   #1000 g = 1 kg
    print(f"{value} g is equal to {round(result, 2)} kg")
    result = value * 0.00220462   #g to lb   #1 g = 0.00220462 lb
    print(f"{value} g is equal to {round(result, 2)} lb")
elif unit == "lb":
    result = value * 0.453592      #lb to kg   #1 lb = 0.453592 kg 
    print(f"{value} lb is equal to {round(result, 2)} kg")
    result = value * 453.592       #lb to g    #1 lb = 453.592 g  
    print(f"{value} lb is equal to {round(result, 2)} g")
else:
    print("Invalid unit")
    
    