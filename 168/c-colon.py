# -*- coding: utf-8 -*-

import math

a, b, h, m = (int(x) for x in input().split())

# if h == 0: #1時まで
#     angle = math.radians(5.5*m)
# else:
#    angle = math.radians(h*30-5.5*m)

angle = math.radians(h*30-5.5*m)

x = math.sqrt(a**2+b**2-2*a*b*math.cos(angle))
print(x)
