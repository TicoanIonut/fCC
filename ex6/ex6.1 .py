fruit = 'abcde'
index = -1
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index-1
    if index < -5:
        quit()
