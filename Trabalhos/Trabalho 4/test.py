#!/usr/bin/env python3
from decimal import *
getcontext().prec = 100
pi1 = Decimal(104348)/Decimal(33215)
pi2 = 104348./33215.
print(Decimal(1/3))
print(Decimal(1)/Decimal(3))
j0_1 = Decimal("0.22389077914123566805182745464994862582515448221861")
j0_2 = Decimal(0.22389077914123566805182745464994862582515448221861)
print(j0_1)
print(j0_2)
print(j0_1-j0_2)