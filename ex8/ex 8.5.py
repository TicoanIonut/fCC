words = open('../long.txt', 'r')
for line in words:
    if line.startswith('From '):
        line = line.split()
        print(line[2])
        