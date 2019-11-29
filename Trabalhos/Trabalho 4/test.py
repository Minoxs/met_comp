#!/usr/bin/env python3
from decimal import *
getcontext().prec = 10000
pi1 = Decimal(104348)/Decimal(33215)
pi2 = 104348./33215.
print(pi2,pi1)
