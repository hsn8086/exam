from math import ceil

for _ in range(int(input())):
    n = int(input())
    pair = list()
    for a,b in zip(map(int, input().split()), map(int, input().split())):
        pair.append([a,b,0])
    sp = sorted(pair, key=lambda t: t[0])
    same_cnt = 0

    for a, b,_ in sp:
        
        if a == b:
            if same_cnt:
                print(-1)
                break
            same_cnt += 1

        if sp[b - 1][1] != a:
            print(-1)
            break

    else:
        rem=set()
        id_=0
        for i in range(n):
            if pair[i][0] not in rem:
                if pair[i][0]==pair[i][1]:
                    pair[i][2]=ceil(n/2)-1
                else:
                    rem.add(pair[i][1])
                    pair[i][2]=id_
                    sp[pair[i][1]-1][2]=-id_-1
                    id_+=1
        cnt=1
        rst=[]
        while cnt:
            cnt=0
            for i in range(n):
                _,_,idx_ = pair[i]
                if idx_<0:
                    idx=n+idx_
                else:
                    idx=idx_
                if i!=idx:
                    rst.append((i+1,idx+1))
                    pair[i],pair[idx]=pair[idx],pair[i]
                    cnt+=1
        print(len(rst))
        for i in rst:
            print(*i)
        # rst = []
        # mid = n // 2+1
        # cnt = 1
        # while cnt:
        #     cnt =0
        #     for i in range(n):
        #         a, b = pair[i]
        #         if b >= mid and i + mid  != b:
        #             # print(b, mid, i)
        #             rst.append((i + 1, b - mid + 1))
        #             # cnt+=1
        #             pair[i], pair[b - mid ] = pair[b - mid ], pair[i]
        #         if a>=mid and n-i-1+mid!=a:

        #             rst.append((i + 1, n+mid-a))
        #             # cnt+=1
        #             print(a,mid,i)
        #             pair[i], pair[ n-1+mid-a] = pair[ n-1+mid-a], pair[i]
        # print(pair)
