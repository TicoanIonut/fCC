lll = []
while True:
    inp = input('enter number  ')
    if inp == 'done':
        break
    try:
        iinp = float(inp)
        lll.append(iinp)
    except ValueError:
        print('Bad data')

print(max(lll), min(lll))
