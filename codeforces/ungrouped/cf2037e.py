def query(i,j):
    print(f"? {i} {j}")
    return int(input())


ntc = int(input())
arr = [1]

for _ in range(ntc):
    n = int(input())
    for i in range(1, n):
        if query(i,i+1) == 1:
            arr.append(1 if arr[-1] else 0)

        else:
            arr.append(0 if arr[-1] else 1)
    count = sum(arr)
    target = query(1, n)
    if count == target:
        print(" ".join(map(str, arr)))
    else:
        print(" ".join(map(lambda x: "0" if x == 1 else "1", arr)))
