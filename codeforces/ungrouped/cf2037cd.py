from itertools import product, count, permutations


def is_prime(n):
    if n <= 1:
        return False 
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False 
    return True  

ntc=int(input())
for _ in range(ntc):
    n=int(input())
    found=False
    for i in permutations(range(1,n+1), n):
        lst=list(i)
        for j in range(1,len(i)):
            if is_prime(lst[j-1]+lst[j]):
                break    
        else:
            print(" ".join(map(str,lst)))
            found=True
            break
        if found:
            break
    else:
        print(-1)
