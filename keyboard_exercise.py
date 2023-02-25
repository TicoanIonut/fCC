# KEYBOARD PROBLEM
# Each day, to enter their building, employees of an e-commerce company have to type a string
# of numbers into a console using a 3 x 3 numeric pad. Every day the numbers on the keypad
# are mixed up.
# Use the following rules to calculate the total amount of times it takes to type a string:
# It take 0 seconds to move their finger to the first key, and it takes 0 seconds to press
# the key where their finger is located any number of times.
# They can move their finger from one location to any adjacent key in 1 second, adjacent
# keys include those on a diagonal.
# Moving to a non adjacent key is done as a series of moves to adjacent keys.
#
# Function Description:
# Complete the function entryTime below
# entryTime has the following parameter(s):
#  string s: the string to type
#  string keypad: a string of 9 digits where each group of 3 digits represents a row on the keypad of the day in order
# Returns:
#  int: integer denotating the minimum of times it takes to type the string s.
# Constraints
#  1<=s<=10**5
#  keypad = 9
# keypad[i] is a number from 1 to 9
import random


def entryTime(s, keypad):
    time_taken = 0
    prev_char = None
    for char in s:
        char_index = keypad.index(char)
        if prev_char is not None:
            distance = calc_distance(prev_char, char_index)
            time_taken += distance
        prev_char = char_index
    return time_taken


def calc_distance(char1, char2):
    row_diff = abs(char1 // 3 - char2 // 3)
    col_diff = abs(char1 % 3 - char2 % 3)
    return max(row_diff, col_diff)


def entryTime2(s, keypad):
    key_positions = {}
    for i in range(len(keypad)):
        key_positions[keypad[i]] = (i // 3, i % 3)
    time = 0
    x, y = key_positions[s[0]]
    for i in range(1, len(s)):
        next_x, next_y = key_positions[s[i]]
        time += max(abs(next_x - x), abs(next_y - y))
        x, y = next_x, next_y
    return time


# s = [1, 2, 3, 4]
# keypad = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = [random.randint(1, 9) for _ in range(random.randrange(5, 11))]
code = ''.join(map(str, s))
print(f'The code is {code}')
keypad = random.sample(range(1, 10), 9)
print(f'The keypad is\n'
      f'{keypad[0]} | {keypad[1]} | {keypad[2]}\n'
      f'{keypad[3]} | {keypad[4]} | {keypad[5]}\n'
      f'{keypad[6]} | {keypad[7]} | {keypad[8]}')


result = entryTime(s, keypad)
result2 = entryTime2(s, keypad)
print(f'The minimum numer of seconds to enter the code is\nfirst func {result}\nsecond func {result2}')






