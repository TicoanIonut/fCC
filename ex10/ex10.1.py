lll = []
while len(lll) < 5:
    inp = input(' Enter text   ').lower()
    if inp == 3:
        break
    if inp.isalpha():
        print(inp)
        lll.append(inp)
    else:
        inp = input(' Enter valid text   ').lower()
        if inp == 3:
            break
jj = ''.join(lll)
dd = {}
for i in jj:
    dd[i] = dd.get(i, 0) + 1
rr = sorted((k, v) for k, v in dd.items())
for k, v in rr:
    print(k, v)
