def bubble_sort(nums):
	swapped = True
	while swapped:
		swapped = False
		for i in range(len(nums) - 1):
			if nums[i] > nums[i + 1]:
				nums[i], nums[i + 1] = nums[i + 1], nums[i]
				swapped = True


def selection_sort(nums):
	for i in range(len(nums)):
		lowest_value_index = i
		for j in range(i + 1, len(nums)):
			if nums[j] < nums[lowest_value_index]:
				lowest_value_index = j
		nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


def insertion_sort(nums):
	for i in range(1, len(nums)):
		item_to_insert = nums[i]
		j = i - 1
		while j >= 0 and nums[j] > item_to_insert:
			nums[j + 1] = nums[j]
			j -= 1
		nums[j + 1] = item_to_insert


bidders_num = int(input("Enter the number of bidders: "))
results = []
for n in range(bidders_num):
	results.append(int(input("Enter the number of donuts eaten by participant {}: ".format(n + 1))))

sort_types = {
	1: bubble_sort,
	2: selection_sort,
	3: insertion_sort,
}

results = list(set(results))

sort_type = int(input("Enter sort type:\n"
                      "1 - Outputting the result using Bubble sort\n"
                      "2 - Outputting the result using Sort by selection method\n"
                      "3 - Outputting the result using Insert sort\n"))

sort_types[sort_type](results)
if len(results) > 2:
	print("First place went to the participant who ate {} donuts".format(results[-1]))
	print("Second place went to the participant who ate {} donuts".format(results[-2]))
	print("Third place went to the participant who ate {} donuts".format(results[-3]))
	print("The worst result corresponds to {} donuts".format(results[0]))
else:
	print("You've entered less than 3 unique results")