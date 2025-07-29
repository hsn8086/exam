import sys

while True:
    try:
        inp=sys.stdin.readline()
    except:
        break
    if not inp:
        break
    a,b=map(int,inp)
    print(a+b)