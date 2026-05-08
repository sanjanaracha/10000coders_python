# CONDITIONAL STATEMENTS PROGRAMS

# 1. Check Voting Eligibility

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


# 2. Grade Classification Function

def grade(marks):
    if marks < 50:
        print("Fail")
    elif marks <= 69:
        print("Pass")
    elif marks <= 84:
        print("Good")
    else:
        print("Excellent")

grade(75)


# 3. Simple Calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", a + b)

elif op == "-":
    print("Result:", a - b)

elif op == "*":
    print("Result:", a * b)

elif op == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero")

else:
    print("Invalid operator")


# 4. Leap Year Checker

year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


# 5. Odd or Even Checker

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")