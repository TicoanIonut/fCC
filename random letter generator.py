import random


def key_gen():
    keylist = random.choice('abcdefghijklmnopqrstuvwxyz')
    return keylist


number = 1
list_item = ''
while number < 5:
    number = number + 1
    list_item = list_item + key_gen()
print(list_item)
