#Write a program that takes a list of numbers and makes a new list of only the first and last elements of the given listInput:
# a = [10,20,35,40,50]
# Output: [10, 50]
# Write a program that takes a list of numbers and prints the biggest number. Write this program without max functionInput:
# a = [1,2,5,29,19,13,11]
# Output:            The biggest number is: 29


def first_last(x):
	
	res = []
	res.append(x[0])
	res.append(x[-1])
	return res
	# return [x[0],x[-1]]


a = [10,20,35,40,50]
print(first_last(a))


def max_nr(s):
	max_value = s[0]
	for value in s:
		if value > max_value:
			max_value = value
	return max_value
	# x = sorted(s)
	# return x[-1]


a = [1,2,5,29,19,13,11]
print(max_nr(a))


# Create a query that does return the name of the customer with the most orders
