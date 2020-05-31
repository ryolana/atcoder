# -*- coding: utf-8 -*-
import numpy as np

n = int(input())
s_li = input().split()
num = list(map(int, s_li))

product = np.prod(num)

ans = product

a = 10 ** 18

if ans > a:
    print("-1")
else:
    print(ans)
