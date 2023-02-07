# mas = [23, 'hello', True]
# print(mas[-1])
#
# for i in range(1, 11):
#     print(i)
#
# for n in range(0, 11, 2):
#     print(n)
#
# for j in range(10, 0, -2):
#     if j % 2 == 0:
#         print(j, end = '')

num = int(input())
data = []
while num != 0:
    data.append(num)
    num = int(input())
data.sort()
print(data)