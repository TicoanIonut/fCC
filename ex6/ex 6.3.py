def count():
    word = 'banana'
    cnt = 0
    for letter in word:
        if letter == 'a':
            cnt = cnt + 1
    print(cnt)


count()
