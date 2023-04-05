word = input("Please enter the word or string: ")
stack = []
for letter in word:
    stack.append(letter)
reversed_word = ''
while stack:
    reversed_word += stack.pop()
print(f"Reversed: {reversed_word}")

print(word[::-1])


# chinese_years = {0: "Monkey",1: "Rooster",2: "Dog",3: "Pig",4: "Rat",5: "Ox",
# 	6: "Tiger",7: "Rabbit",8: "Dragon",9: "Snake",10: "Horse",11: "Goat",}
#
# year = int(input("Enter the year (positive value and less than 10000): \n"))
# while not 0 <= year < 10000:
# 	print("Enter the correct value")
# 	year = int(input("Enter the year (positive value and less than 10000): "))
#
# k = year % 12
# print(f"{year} - The year of the {chinese_years[k]}.")