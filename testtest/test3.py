# if __name__ == '__main__':
#     n = int(input().strip())
# if n%2 !=0:
#     print('Weird')
# elif n%2 == 0 and n in range (2,6) :
#     print('Not Weird')
# elif n%2 == 0 and n in range(6,21):
#     print('Weird')
# elif n%2 == 0 and n>20:
#     print('Not Weird')


n = int(input())
r = []
for j in range(n+1):
	r.append(j)
x = "".join(str(i) for i in r)
print(x)
