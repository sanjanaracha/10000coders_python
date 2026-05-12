# Task : 

# Method: append()
# EASY QUESTIONS
# What happens to the length of a list after calling the append() method?
'''length of list will be increased by 1'''
# Where is the new element placed when you use list.append(x)?
'''at the end of the list'''
# Write a simple line of code to add the string 'apple' to a list named 'fruits'.
'''fruits=['banana']
fruits.append('apple')
print(fruits)'''


# MEDIUM QUESTIONS
# If you append a list [10, 20] to an existing list [1, 2], what is the total number of elements in the final list?

'''a=[1,2]
a.append([10,20])
print(a)

#total elements=3
'''
# Explain the difference in result between list.append([5, 6]) and list + [5, 6].
'''
list.append([5, 6]) adds the entire list as one nested element
list + [5, 6] adds elements separately add creates a new list 
'''
# Method: extend()
# EASY QUESTIONS
# Does the extend() method add elements individually or as a single nested object?
'''It adds elements individually.'''
# What type of argument (e.g., integer, iterable) does the extend() method expect?
'''An iterable (list, tuple, string, set, etc.)'''
# How do you merge list B into list A using extend()?

'''a=[1,2]
b=['a',4]
a.extend(b)
print(a)'''
# MEDIUM QUESTIONS
# Predict the output: my_list = [1, 2]; my_list.extend('34'); print(my_list).
'''[1,2,'3','4']'''

# What is the difference between extend() and the += operator for lists, if any?
'''For lists, both work similarly by adding elements individually.

a = [1, 2]
a.extend([3, 4])
# [1, 2, 3, 4]

a = [1, 2]
a += [3, 4]
# [1, 2, 3, 4]

Difference: += is an operator, extend() is a method.
'''

# Method: insert()
# EASY QUESTIONS
# How many arguments does the insert() method take?
'''2 arguments
(index,element)'''
# If you want to add an element at the very beginning of a list, what index should you use in insert()?
'''use index 0
# a.insert(0, 'x')'''

# Does insert() replace the existing element at the given index or shift it?
'''It shifts existing elements to the right.'''

# MEDIUM QUESTIONS
# What happens if you use a negative index, like list.insert(-1, 'x'), on a list of 3 items?
'''It inserts before the last element.'''
'''a = [1, 2, 3]
a.insert(-1, 'x')
print(a)'''
# In terms of performance, why is insert(0, x) considered slower than append(x) for large lists?

'''Because insert(0, x) shifts all existing elements one position to the right, while append(x) simply adds at the end.

So append() is faster.'''