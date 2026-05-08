for i in "sanjana":
    print(i)

for i in [1,2,3,4,5,6,7,8,9,10]: 
    print(i)

for i in (1,2,3,4,5,6,7,8,9,10): 
    print(i)

for i in range(1,11):
    print(i)

'''
for i in {"id":1,"name":"sanju"}:
    print(i)

    #o/p:id name
for i in {"id":1,"name":"sanju"}.keys():
    print(i)'''

for i in {"id":1,"name":"sanju"}.values():
    print(i)

    #o/p:1 sanju

for i in {"id":1,"name":"sanju"}.items():
    print(i)  

    '''o/p:('id', 1)
           ('name', 'sanju')'''

#-----------------------------
for i,j in {"id":1,"name":"sanju"}.items():
    print(i,j)

    '''id 1
       name sanju'''
print("----------------------")

'''while syntax'''
#while condition:
     #code

# wac to print 1-10 while loop
i=1
while(i<=10):
    print(i)
    i+=1

# using forloop
for i in range(1,11):
    print(i)

# -20 to-30
print("----------------------")
i=-20
while(i>=-30): 
    print(i)
    i-=1


#--------------------------------------

#waq to print only even numbers from 10-1 range in for loop
for i in range(10,0,-1):
    if i%2==0:
        print(i)    
'''o/p:10
8
6
4
2
'''
#----------------------------------------------
#waq to print sum of even numbers from 10-1 range in for loop 
sumofeven=0
for i in range(10,0,-1):
    if i%2==0:
        sumofeven+=i
    print(sumofeven)
            
'''o/p:30'''
#-------------------------------

sumofeven=0
sumofodd=0
for i in range(10,0,-1):
    if i%2==0:
        sumofeven+=i
    else:
        sumofodd+=i
print(sumofeven,"even")
print(sumofodd,"odd")

'''o/p:30 even
       25 odd'''

#-------------------------------
#waq to find vowels in str and count
vowels="aeiouAEIOU"
name="sanjaena"
count=0
for i in name:
    if i in vowels:
        count+=1
        print(i,end=" ")
print(count)

'''o/p:a a e a 4'''

#-----------------------------
# wac to print 11 -100 while loop


for i in range(-1,-100,-1):
    print(i)
'''o/p :prints -1 to -99 '''

# wac to print 11 -100 while loop


for i in range(-100,-1,1):
    print(i)
'''o/p :prints -100 to -2 '''
#--------------------------------
#sum of conjugative nums 
'''n=123 #1+2+3=6
r=str(n)
s=0
for i in r:
    s+=int(i)
print(s,"sum")'''

#while loop :... finding sum of digits in the  number
'''n=123
res=0
while(n!=0):
    digit=n%10  #to get last digit
    res=res+digit #add to sum
    n=n//10       #to remove last digit
print(res,"sum")'''

#------------------------------------------------

# reverse a no. using while loop
n = int(input("Enter number: "))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reversed number:", rev)

# while reversing find sum of even no. and sum of odd numbers

n = int(input("Enter number: "))
rev = 0
sum_even = 0
sum_odd = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit

    if digit % 2 == 0:
        sum_even += digit
    else:
        sum_odd += digit

    n = n // 10

print("Reversed:", rev)
print("Sum of even digits:", sum_even)
print("Sum of odd digits:", sum_odd)

'''o/p:'''
# by using while print 5 divisors upto 100 from 1  

i = 1

while i <= 100:
    if i % 5 == 0:
        print(i, end=" ")
    i += 1

    '''o/p:5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100'''
#--------------------------------------

#waq to print sum of even,odd numbers from 1-10 range in while loop 
sumofeven=0
sumofodd=0
i=1
while (i<=10):
    if i%2==0:
        sumofeven+=i
        
    else:
        sumofodd+=i
    i+=1
print(sumofeven,"even")
print(sumofodd,"odd")

'''o/p:30 even
       25 odd'''

#----------------------------------

#waq to print product of even,odd numbers from 1-10 range in while loop 
productofeven=1
productofodd=1
i=1
while (i<=10):
    if i%2==0:
        productofeven*=i
        
    else:
        productofodd*=i
    i+=1
print(productofeven,"even")
print(productofodd,"odd")

'''o/p:3840 even
945 odd
'''


            
