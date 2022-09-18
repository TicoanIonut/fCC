import random
lower = 'abcdefghijklmnopqrstyuvxz'
upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
number = '1234567890'
symbol = "?!;:'*/)(+-&_$#@"
al = lower+upper+number+symbol
lenght = 13
password = "".join(random.sample(al, lenght))
print('Password:', password)
