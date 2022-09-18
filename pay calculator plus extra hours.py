def computepay(hours, rate):
    print('In computepay', hours, rate)
    if hours > 40:
        print('overtime')
        reg = hours * rate
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    print('Returning', pay)
    return pay


xh = input('enter hours ')
xr = input('enter rate ')
fh = float(xh)
fr = float(xr)
print('hours', fh, 'rate', fr)
xp = computepay(fh, fr)
print('pay', xp)
