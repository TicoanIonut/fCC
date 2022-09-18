stringul = 'X-DSPAM-Confidence: 0.8475'
cc = stringul.find(':')
print(cc)
bb = stringul.find(' ', cc)
print(bb)
aa = stringul[cc + 1:]
print(aa)
zz = float(aa)
print(zz)
