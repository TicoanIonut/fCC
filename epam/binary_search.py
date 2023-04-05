
def binary_search(arr, left, right, elem):
	while left <= right:
		mid_index = (right + left) // 2
		if arr[mid_index] == elem:
			return arr[mid_index]
		elif arr[mid_index] < elem:
			left = mid_index + 1
		else:
			right = mid_index - 1
	return None


library_num = [108, 123, 124, 235, 285, 379, 456, 476, 756, 998]
print("The list of the library card numbers are", library_num)
required_num = int(input("Enter the library card number: "))
if required_num > 0:
	amount = binary_search(library_num, 0, len(library_num) - 1, required_num)
	if amount is None:
		print("\nThe reader is not registered in the library.")
	else:
		print("The reader", amount, "is registered in the library and took book(s).")
else:
	print("You entered an invalid customer library card number.")