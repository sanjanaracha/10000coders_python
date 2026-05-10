# Implement a function that takes a list of numbers as input and returns the average of these numbers.

def avgnums():
    n=eval(input())
    sum=0
    for i in n:
        sum+=i
    avg= sum/(len(n))
    print(int(avg))
avgnums()


# Create a function that accepts a string and returns the string with all vowels removed.

def consonents(n):
    v="aeiouAEIOU"
    result=""
    
    for i in n:
        if i not in v:
            result+=i
    print(result)
consonents(input("enter string:"))

# Develop a function to find and return the maximum value in a given list of integers.

'''def maxi(n):
    n.sort()
    print(n)
    
    print(n[len(n)-1])
n=list(map(int,input().split()))
maxi(n)'''


def maxi(n):
    max_ele=n[0]
    for i in n:
        if i>max_ele:
            max_ele=i
    print(max_ele)

n=list(map(int,input().split()))
maxi(n)



# Design a function that simulates a basic calculator, allowing for addition, subtraction, multiplication, and division based on user input.
def calculator(a,b):
    
    print("1.addition")
    print("2.subtraction")
    print("3.multiplition")
    print("4.division")
    ch=int(input("choose your choose"))
    

    if ch==1:
        print(a+b)
    elif ch==2:
        print(a-b)
    elif ch==3:
        print(a*b)
    elif ch==4:
        print(a/b)
    else:
        print("enter a valid choice")
a=int(input("enter no."))
b=int(input("enter no."))
calculator(a,b)

# Write a function that takes a list of strings as input and returns the longest string in the list.

def longeststr(n):
    # print(n)
    h=len(n[0])
    longest=n[0]
    for i in n:
        if len(i)>h:
            h=len(i)
            longest=i
    print(longest)

n=input().split()
longeststr(n)


# Utilize functions to solve a problem of your choice (e.g., calculating the area and perimeter of different shapes, converting units, etc.), demonstrating your understanding of how functions can be applied in various contexts.


def rectangle(length,width):
    area=length*width
    perimeter=2*(length+width)
    print("area:",area)
    print("perimeter:",perimeter)

def square(side):
    area=side*side
    perimeter=4*side
    print("area:",area)
    print("perimeter:",perimeter)

def circle(radius):
    area=3.14*(radius**2)
    perimeter=2*3.14*radius
    print("area:",area)
    print("perimeter:",perimeter)

choice=input("enter shape:")
if choice=="rectangle":
    l=float(input("enter length:"))
    w = float(input("Enter width: "))
    rectangle(l, w)

elif choice=="square":
    s=float(input("enter side:"))
    square(s)
elif choice=="circle":
    r=float(input("enter radius:"))
    circle(r)
else:
    print("invalid choice")