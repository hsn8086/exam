import sys
from decimal import setcontext, Context, Decimal

setcontext(Context(prec=2000000, Emax=2000000, Emin=0))
a, b = map(Decimal, sys.stdin.readlines())

print(a * b)
