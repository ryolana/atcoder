# -*- coding: utf-8 -*-

from decimal import Decimal

a, b = input().split()

print(int(Decimal(a)*Decimal(b)))
