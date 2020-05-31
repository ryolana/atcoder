# -*- coding:utf-8 -*-

s, w = (int(x) for x in input().split())

if w >= s:
    print("unsafe")
else:
    print("safe")
