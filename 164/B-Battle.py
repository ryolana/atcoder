# -*- coding:utf-8 -*-

a, b, c, d = (int(x) for x in input().split())


while a > 0 and c > 0:
    c = c - b
    if c <= 0:
        print("Yes")
    else:
        a = a - d
        if a <= 0:
            print("No")



# while a > 0:
#     c = c - b
#
