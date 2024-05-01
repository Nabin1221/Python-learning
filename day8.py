#Datatype methods
a = 'Hello'

print(type(a))


#String methods
a = 'hello world'

b = a.capitalize()

print(b)

#List methods
a = [1,2,3,4,'Hello','Python']

print(a)

a.insert(1,'Hello')

print (a)

#Tuple methods
a = (1,2,3,4,'Hello')

b = a.index('Hello')

print (b)

#Set methods
a = {1,2,3,4,5}
b = {4,5,6,7,8}

b.difference_update(a)

print (b)

# Dictionary methods
a= { 'a':'Hello','b':'World'}

b = a.get(1)

print (b)

# Task : Login program
# Requirements
# Make a dictionary data containing username as key and password as value
# Ask user for password
# Ask user for password
# If the username and password exists in a dictionary data print login success
# Else print Invalid credentials

# Medium level task : Login
# Requirements
# Make a list of usernames
# Ask user for username
# 
