def is_prime(n):
    if n <= 1:
        return False 
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False 
    return True  

ntc=int(input())
for _ in range(ntc):
    n = int(input())
    if n <= 4:
        print(-1)
    elif n==5:
        print("1 3 5 4 2")
    else:
        even_nums = [2]+[i for i in range(6, n+1, 2)]+[4]
        odd_nums = [5,1,3]+[i for i in range(7, n+1, 2)]

        perm = even_nums + odd_nums
        print(' '.join(map(str, perm)))
