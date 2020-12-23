#!/usr/bin/env python3

#Iterative version

def fibonacci(n):
	if (n==0):
		return 0
	else:
		fiblist = [0, 1]
		newNum = 0
		for n in range(1,n):
			newNum = fiblist[n-1] + fiblist[n]
			fiblist.append(newNum)
		return fiblist[n+1]

print(fibonacci(7))

# Recursive version


def fibonacci(n):
	if n < 0:
		ValueError("Input 0 or greater only!")
	if n <= 1:
		return n
	return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(3)
# 2
fibonacci(7)
# 13
fibonacci(0)
# 0
