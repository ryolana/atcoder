# -*-  coding:utf-8 -*-

N = int(input())

A = N % 10

if A == 2 or A == 4 or A == 5 or A == 7 or  A == 9:
    print("hon")
elif A == 3:
    print("bon")
else:
    print("pon")
