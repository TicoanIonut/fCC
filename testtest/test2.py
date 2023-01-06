# import requests
# import pandas as pd
# response = requests.get("http://api.open-notify.org/astros.json")
# # print(response.status_code)
# # print(response.json())
# res = pd.DataFrame(response.json()["people"])
# print(res.head())
# print(res)


# def fizzBuzz(nnn):
#     for n in range(nnn):
#         if n % 3 == 0 and n % 5 == 0:
#             print('FizzBuzz')
#         elif n % 3 == 0:
#             print('Fizz')
#         elif n % 5 == 0:
#             print('Buzz')
#         else:
#             print(str(n))
# if __name__ == '__main__':
#     nnn = int(input().strip())
#     fizzBuzz(nnn)


# def miniMaxSum(arr):
#     arr.sort()
#     min = sum(arr[0:4])
#     max = sum(arr[1:5])
#     print(f'{min} {max}')
# if __name__ == '__main__':
#     arr = list(map(int, input().rstrip().split()))
#     miniMaxSum(arr)


# def timeConversion(s):
#     if (s[-2:] == 'AM'):
#         if (s[:2] == '12'):
#             return '00' + s[2:-2]
#         else:
#             return s[:-2]
#     else:
#         h = int(s[:2])
#         if h < 12:
#             h += 12
#         return str(h) + s[2:-2]
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     s = input()
#     result = timeConversion(s)
#     fptr.write(result + '\n')
#     fptr.close()


# def plusMinus(arr):
#     l = len(arr)
#     result = [0, 0, 0]
#     for a in arr:
#         if a < 0:
#             result[1] += 1
#         elif a > 0:
#             result[0] += 1
#         else:
#             result[2] += 1
#     for i in range(3):
#         result[i] /= l
#     print(result[0])
#     print(result[1])
#     print(result[2])
# if __name__ == '__main__':
#     n = int(input().strip())
#     arr = list(map(int, input().rstrip().split()))
#     plusMinus(arr)

