n=int(input())

def is_divisor(a, b):
    return b != 0 and a % b == 0

for _ in range(n):
    x, m = map(int, input().split())
    count = 0
    
    for y in range(1, min(m + 1, x*2+1)):
        if y == x:
            continue
        
        xor = x ^ y

        if (is_divisor(x, xor) or is_divisor(y, xor)):
            count += 1




    print(count)
