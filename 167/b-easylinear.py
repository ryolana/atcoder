# -*- coding: utf-8 -*-

a, b, c, k = (int(x) for x in input().split())

if k <= a:
    print(k)
elif k <= a + b:
    print(a)
else:
    print(a + k - c - b)
