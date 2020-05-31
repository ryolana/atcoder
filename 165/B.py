# -*- coding: utf-8 -*-

x = int(input())

y = 100
i = 0

while y < x:
    y = y + y // 100  #小数点以下を切り捨てる時はy = y*1.01ではだめ。
    i = i + 1

print(i)
