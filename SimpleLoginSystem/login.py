username=input("Enter your username: ")
password=int(input("Enter your password: "))

if username == "admin" and password == 1234:
    print("Login Successful!")

else:
    print("Invalid username or password")
