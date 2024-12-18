jd={
    1:1,
    2:2,
    3:2,
    4:2,
}
ntc=int(input())
for _ in range(ntc):
    req=int(input())
    if req in jd:
        print(jd[req])
        continue
    now=4
    count=2
    while now<req:
        now=(now+1)*2
        count+=1
    print(count)