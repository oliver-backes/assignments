#!/usr/bin/env python2

base = input('Enter your base: ')

exponent = input('Enter your exponent: ')

#This portion of the code defines the square_n_times functon
def square_n_times(number,n):
	square = number
	for x in range(0,n-1):
		square *= number
	return square

#This portion of the code calls the square_n_times function and provides an explanation
print "I'm going to use the calculator function to raise %s to the power of %s:" % (base, exponent)
x = square_n_times(base,exponent)
print x