#!/usr/bin/env python3

#Factorial iterative and recursive function


def factorial(n): 
	counter = 1
	for n in range(1,n+1):
		counter = counter * n
	return counter
		
	

def factorial_rec(n):  
	if n < 0:    
		ValueError("Inputs 0 or greater only") 
	if n <= 1:    
		return 1  
	return n * factorial(n - 1)

print(factorial(3) == 6)
print(factorial(0) == 1)
print(factorial(5) == 120)

factorial(8)
