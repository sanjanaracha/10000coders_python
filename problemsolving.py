'''1. Write a python program to remove the duplicate in given list.
                a = [2,3,4,2,3,4,5,7]
                output: [2,3,4,5,7]'''

a=[2,3,4,2,3,4,5,7]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)


'''2. Write a program that takes array of numbers as input, 
among the numbers in array, print the numbers which forms a prime number by adding one to it.
Print such numbers in the given array separated b spaces.

              Testcase1	:  [ 7, 4, 7, 23, 10, 6]
               Output     	:  4 10 6'''


a=eval(input())
for i in a:
    n=i+1
    for j in range(2,n):
        if n%j==0:
            break
    else:
        print(j)
'''3. Write python program 
              a   = " aaabbaaccdd"
             output: "a5b2c2d2"'''

'''a="aaabbaaccdd"
for i in set(a):
    print(i+str(a.count(i)),end="")'''

a   = "aaabbaaccdd"
b=""
for i in a:
    if i not in b:
        print(i + str(a.count(i)), end="")
        b+=i
