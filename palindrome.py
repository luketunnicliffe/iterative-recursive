
#Iterative

def is_palindrome(my_string):
	while len(my_string) > 1:
		if my_string[0] != my_string[-1]:
			return False
		my_string = my_string[1:-1]
	return True 

palindrome("abba")
# True
palindrome("abcba")
# True
palindrome("")
# True
palindrome("abcd")
# False


#Recursive

def is_palindrome(my_string):
	print(my_string)
	
	if len(my_string) > 3:
		if my_string[0] != my_string[-1]:
			return False
		else:
			is_palindrome(my_string[1:-1])
	
	return True




print(is_palindrome("abba") == True)
print(is_palindrome("abcba") == True)
print(is_palindrome("") == True)
print(is_palindrome("abcd") == False)
