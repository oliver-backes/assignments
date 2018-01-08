#!/usr/bin/env python2

# This portion of the code defines the multiply function 
def multiply(a,b):
	return a * b 

# This portion of the code defines the add function
def add(a,b):
	return a + b

#This portion of the code defines the subtract function
def subtract(a,b):
	return a - b

#This portion of the code defines the divide function
def divide(a,b):
	return a / b

#This portion of the code defines the square function
def square(a):
	return a * a

#This portion of the code defines the cube function
def cube(a):
	return a * a * a

#This portion of the code defines the square_n_times functon
def square_n_times(number,n):
	for x in range(0,n):
		number = square(number)
		return number

#This portion of the code calls the multiply function and provides an explanation
print "I'm going to use the calculator function to multiply 2 and 36:"
x = multiply(2,36)
print x

#This portion of the code calls the square_n_times function and provides an explanation
print "I'm going to use the calculator function to square 2 three times"
y = square_n_times(2,3)
print y