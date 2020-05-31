# -*-  coding:utf-8 -*-

k = int(input())
s = input()

l = len(s)

if l <= k:
    print(s)
else:
    m = s[0:k]
    print(m+"...")
