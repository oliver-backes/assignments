#!/usr/bin/env python2
import sys

inputs = []

base = raw_input('Enter your base: ')

inputs.append(base)

exponent = raw_input('Enter your exponent: ')

inputs.append(exponent)

print inputs

for input in inputs:
	if not (input.isdigit()):
		sys.exit(input + " is not a number.")

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