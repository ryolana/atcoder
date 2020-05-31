# -*- coding: utf-8 -*-

K = int(input())
A, B = (int(x) for x in input().split())

#倍数が何個含まれるかで考える場合
# a = A // K
# b = B // K
#
# if b-a >= 1 or K == 1:
#     print("OK")
# elif B%K==0 or A%K==0:
#     print("OK")
# else:
#     print("NG")

#B以下の最大のKの倍数がAを超えるかどうかで考える場合
#B以下の最大のkの倍数
maxbk = (B//K)*K

if maxbk >= A:
    print("OK")
else:
    print("NG")
