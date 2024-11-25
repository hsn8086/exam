def count(a:list[int],n:int)->int:
    sum = 0
    for i in range(n):
        for j in range(i):
            if a[j] > a[i]:
                sum += 1

    return sum
