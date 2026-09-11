num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))

op=input("Choose an operation (+, -, *, /): ")

if op == "+":
    print("Addition: ", num1+num2)
elif op == "-":
    print("Subtraction: ", num1-num2)
elif op == "*":
    print("Multiplication: ", num1*num2)
elif op == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero")
    else:
        print("Division: ", num1/num2)
else :
    print("Invalid input")
