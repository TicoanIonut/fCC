file = open('../romeo.txt', 'r')
for line in file:
    line = line.split()
    ss = set(line)
    print(sorted(ss))
    