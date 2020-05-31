# -*- coding:utf-8 -*-

s = input()
s_len = len(s)

odd = s[::2] #スライスを利用してsの奇数番目を取り出す
even = s[1::2]

if "L" in odd:
    print("No")
elif "R" in even:
    print("No")
else:
    print("Yes")
