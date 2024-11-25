import itertools

for a in itertools.permutations(range(1,10),r=9):
    fir=a[:3]
    sec=a[3:6]
    thi=a[6:9]
    print(fir,sec,thi)