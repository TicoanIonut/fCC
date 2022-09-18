words = open('../long.txt', 'r')
ddict = dict()
for line in words:
    if line.startswith('From '):
        lines = line.split()
        ddict[lines[2]] = ddict.get(lines[2], 0) + 1
print(ddict)

words = open('../long.txt', 'r')
ddict = dict()
for line in words:
    if line.startswith('From '):
        lines = line.split()
        ddict[lines[1]] = ddict.get(lines[1], 0) + 1
print(ddict)
