smallest = None
largest = None
num = 0
tot = 0.0
while True:
    sval = input("enter a number\t")
    if sval == 'done':
        break
    try:
        fval = float(sval)
        if largest is None:
            largest = fval
        elif fval > largest:
            largest = fval
        if smallest is None:
            smallest = fval
        elif fval < smallest:
            smallest = fval
    except ValueError or ZeroDivisionError:
        print('bad data')
        continue
    num = num+1
    tot = tot+fval
print('all done')
print('total', tot, '\nnumbers', num, '\ntotal/numbers', tot/num)
print("Largest value is", largest)
print("Smallest value is", smallest)
