
'''creates 3 functions and create every function scoped variables in them and 
create 3 global variables and try to access global variables in every function and 
try to access every function variables in functions and 
try to access function variables outside of the function
'''

x=100
class hello():
    b="how are you"
    def animal(self):
        self.a="lion"
        self.age=20
        print(self.a) #local scope
        print(hello.b) #class scope
        print(x)  #global scope


    def bird(self):
        # a="parrot"
        # age=4
        pass
        print(x)
        # print(self.a,self.age) #instance scope (object scope)


    def human(self):
        a="ramu"
        age=70
        print(x)
c=hello()
c.animal()
c.bird()



'''Here are 15 theory questions on Functions in Python:

Basic Theory Questions'''
# What is a function in Python?
'''A function is a reusable block of code that performs a specific task.

Example:

def greet():
    print("Hello")
'''
# Why are functions used in programming?
'''Functions are used to:

Reuse code
Reduce code repetition
Make code organized
Improve readability
Make debugging easier
'''
# What is the syntax for defining a function in Python?
'''def function_name(parameters):
    # code
    return value

Example:

def add(a, b):
    return a + b
'''
# What is the purpose of the def keyword in Python?
'''def is used to define (create) a function.

Example:

def hello():
    print("Hi")
'''
# What is the difference between a function definition and a function call?

'''Function Definition: Creating the function

def greet():
    print("Hello")

Function Call: Executing the function

greet()'''
# Intermediate Theory Questions

# What are parameters and arguments in Python functions?

'''Parameters: Variables in function definition
Arguments: Values passed during function call

Example:

def add(a, b):   # parameters
    print(a+b)

add(2, 3)        # arguments'''
# What is the difference between formal parameters and actual parameters?
'''Formal Parameters: Variables in function definition
Actual Parameters: Real values passed in function call

Example:

def show(name):   # formal parameter
    print(name)

show("Sanjana")   # actual parameter'''

# What is a return statement in a function?
'''return sends a value back from the function.

Example:

def square(n):
    return n*n'''

# What happens if a Python function does not have a return statement?
'''It returns None by default.

Example:

def test():
    print("Hello")

x = test()
print(x)

Output:

Hello
None'''

# What are default arguments in Python functions?
'''Default values assigned to parameters.

Example:

def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Sanjana")

Output:

Hello Guest
Hello Sanjana'''


# Advanced Theory Questions
# What are keyword arguments in Python?
'''Arguments passed using parameter names.

Example:

def student(name, age):
    print(name, age)

student(age=21, name="Sanjana")'''

# What are variable-length arguments (*args and **kwargs) in Python functions?
'''*args → accepts multiple positional arguments

Example:

def add(*nums):
    print(sum(nums))

add(1,2,3,4)

**kwargs → accepts multiple keyword arguments

Example:

def details(**data):
    print(data)

details(name="Sanjana", age=21)'''

# What is the difference between local variables and global variables in functions?
'''Local Variable: Inside function, usable only there

def test():
    x = 10

Global Variable: Outside function, usable everywhere

x = 10

def test():
    print(x)'''

# What are recursive functions in Python?
'''A function that calls itself.

Example:

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)'''

# What are lambda (anonymous) functions in Python?
'''Small functions without a name, created using lambda.

Syntax:

lambda arguments : expression

Example:

square = lambda x: x*x
print(square(5))

Output:

25'''

