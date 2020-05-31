# -*- coding: utf-8 -*-

n = int(input())
# s_li = input().split()
# num = list(map(int, s_li))
#
# product = 1
#
# for i in range(n):
#     if  num[i-1] == 0:
#         product = 0
#         break
#     if product != -1:
#         product = product * num[i-1]
#         if product > 10**18:
#             product = -1
#             break

a_li = list(map(int, (input().split())))

product = 1

if 0 in a_li:
    product = 0
else:
    for i in a_li:
        product *= i
        if product > 10**18:
            print(-1)
            exit()

print(product)
