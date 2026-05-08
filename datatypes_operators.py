# PART 4: type() Function

# 21. What does type() function do?
# Answer: The type() function is used to find the data type of a variable.

x = 25
print(type(x))

# 22. What is output of:
x = 25
print(type(x))
# Output: <class 'int'>

# 23. What is output of:
x = "100"
print(type(x))
# Output: <class 'str'>

# 24. Write a program to print type of a variable entered by user.
x = input("Enter something: ")
print(type(x))


# PART 5: input() Function

# 25. What does input() function return by default?
# Answer: input() returns a string (str) by default.

# 26. Write a program to take user name and print it.
name = input("Enter your name: ")
print("Your name is:", name)

# 27. Take two numbers from user and print their sum.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum is:", a + b)

# 28. What happens if you add two numbers taken by input() without casting?
# Answer: It concatenates strings instead of performing numerical addition.

a = input("Enter first number: ")
b = input("Enter second number: ")
print(a + b)


# PART 6: Type Casting

# 29. Convert string "100" to integer.
x = int("100")

# 30. Convert integer 25 to string.
x = str(25)

# 31. Convert float 10.8 to int.
x = int(10.8)

# 32. Write a program to take age from user and convert it to int.
age = int(input("Enter your age: "))
print("Your age is:", age)


# BONUS Logical Questions

# 33. Predict output:
x = "5"
y = "10"
print(x + y)
# Output: 510

# 34. Predict output:
x = int("5")
y = int("10")
print(x + y)
# Output: 15

# 35. What will happen?
# Answer: ValueError occurs

# int("hello")