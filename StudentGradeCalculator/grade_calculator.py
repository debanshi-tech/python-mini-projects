marks = float(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")

elif marks < 50:
    print("F")

elif marks >= 50 and marks <= 59:
    print("D")

elif marks >= 60 and marks <= 69:
    print("C")

elif marks >= 70 and marks <= 79:
    print("B")

elif marks >= 80 and marks <= 89:
    print("A")

elif marks >= 90 and marks <= 100:
    print("A+")
