file = input('enter file name.txt')
if file == 'long.txt':
    file = open('long.txt', 'r')
elif file == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()
elif file != 'long.txt':
    print('File cannot be opened', file)
    quit()
file = open('long.txt', 'r')
lines = file.readlines()
num = 0
tot = 0.0
for line in lines:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        # print(line)
        x = line.find(':')
        # print(x)
        y = line[x+1:]
        z = float(y)
        # print(z)
        num = num + 1
        tot = tot + z
print('total', tot)
print('number of lines', num)
print('average', tot/num)
