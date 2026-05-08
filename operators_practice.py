# PYTHON OPERATORS

# 1. Arithmetic Operators
# (+, -, *, /, %, //, **)

a = 15
b = 4

print(a + b)   # Output: 19
print(a - b)   # Output: 11
print(a * b)   # Output: 60
print(a / b)   # Output: 3.75
print(a % b)   # Output: 3 (remainder)
print(a // b)  # Output: 3 (floor division)
print(a ** b)  # Output: 50625 (15 raised to power 4)


# 2. Comparison Operators
# (==, !=, >, <, >=, <=)

x = 10
y = 20

print(x == y)   # Output: False
print(x != y)   # Output: True
print(x > y)    # Output: False
print(x < y)    # Output: True
print(x >= 10)  # Output: True
print(y <= 15)  # Output: False


# 3. Logical Operators
# (and, or, not)

a = 5
b = 8

print(a > 3 and b > 5)   # Output: True
print(a > 10 or b > 5)   # Output: True
print(not(a > 3))        # Output: False


# 4. Assignment Operators
# (=, +=, -=, *=, /=)

x = 10

x += 5   # x = x + 5 → 15
x *= 2   # x = x * 2 → 30
x -= 10  # x = x - 10 → 20

print(x)  # Output: 20


# 5. Membership Operators
# (in, not in)

name = "Sanjana"

print("a" in name)       # Output: True
print("z" not in name)   # Output: True


# 6. Identity Operators
# (is, is not)

a = [1, 2]
b = [1, 2]

print(a == b)   # Output: True (values are same)
print(a is b)   # Output: False (different memory locations)