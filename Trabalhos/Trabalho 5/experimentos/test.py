from decimal import *

n = "14"
m = "-13"
n = Decimal(n)
m = Decimal(m)
lst = [n,m]
print(lst)
print(n.compare_signal(m))