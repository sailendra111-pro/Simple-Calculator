print(" **CALCULATOR PROGRAM** ")
operators =input("Enter the operator you want to use: +, -, *, /: ")
num1 =float(input("Enter first number: "))
num2 =float(input("Enter second number: "))
if operators =="+":
    result = num1 + num2
    print(round(result,2))
elif operators =="-":
    result = num1 - num2
    print(round(result,2))  
elif operators =="*":
    result = num1 * num2
    print(round(result,2))
elif operators =="/":
    result = num1 / num2
    print(round(result,2))
else:
    print("Invalid operator")