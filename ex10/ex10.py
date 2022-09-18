# words = open('long.txt', 'r')
# ddict = dict()
# for line in words:
#     if line.startswith('From '):
#         lines = line.split()
#         ddict[lines[1]] = ddict.get(lines[1], lines[4])
# lll = sorted((v, k) for k, v in ddict.items())
# for v, k in lll:
#     print(k, v)


words = open('../long.txt', 'r')
ddict = dict()
for line in words:
    if line.startswith('From '):
        lines = line.split()
        # print(lines)
        lin = lines[5].split(':')
        # print(lin)
        ddict[lin[0]] = ddict.get(lin[0], 0) + 1

# print(ddict)
lll = sorted((v, k) for k, v in ddict.items())
for v, k in lll:
    print(k, v)