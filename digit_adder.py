#!/usr/bin/env python3

# Linear - O(N), where "N" is the number of digits in the number
def sum_digits(n):
	if n < 0:
		ValueError("Inputs 0 or greater only!")
	result = 0
	while n != 0:
		result += n % 10
		n = n // 10
	print(result + n)
	return result + n



#sum_digits(12)
# 1 + 2
# 3
#sum_digits(552)
# 5 + 5 + 2
# 12
#sum_digits(123456789)
# 1 + 2 + 3 + 4...
# 45


def sum_digitsR(n):
	result = 0
	if n < 10:
		return n
	while n > 10:
		result = n % 10
		return result + (sum_digitsR(n//10))



print(sum_digitsR(123456789))

print(sum_digitsR(552))

print(sum_digitsR(123456789))


