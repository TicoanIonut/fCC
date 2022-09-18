def chop():
    ttt = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    ttt.pop()
    ttt.pop(0)
    return ttt

print('chop', chop())


def mid(s):
    del s[0]
    del s[-1]
    return mid

lll = [1, 2, 3, 1, 2, 3, 1, 2, 3]
mid(lll)
print('mid', lll)

