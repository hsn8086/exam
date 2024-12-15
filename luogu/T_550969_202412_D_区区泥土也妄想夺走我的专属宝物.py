ntc=int(input())
for _ in range(ntc):
    inp=list(map(int,input().split()))
    a=inp[0]
    submit=inp[1:]
    gt=sum(submit)
    dirt=(a-gt)/a
    print("%.4lf" % dirt)