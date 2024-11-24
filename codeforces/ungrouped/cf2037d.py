from collections import deque
import heapq

def solve(n: int, m: int, k: int, bloks: list, powers: deque):
    now_powers = [] 
    power = 1
    count = 0
    
    for left, right in bloks:

        while powers and powers[0][0] < left:
            pos, value = powers.popleft()
            heapq.heappush(now_powers, (-value, pos)) 
            

        needed_power = right - left + 2 - power
        while needed_power > 0:
            if not now_powers:
                return -1
            value, _ = heapq.heappop(now_powers)
            power -= value  
            count += 1
            needed_power = right - left + 2 - power
            
    return count


ntc = int(input())
for _ in range(ntc):
    n, m, k = map(int, input().split())
    bloks = []
    powers = deque()
    for _ in range(n):
        left, right = map(int, input().split())
        bloks.append((left, right))
    for _ in range(m):
        pos, value = map(int, input().split())
        powers.append((pos, value))

    print(solve(n, m, k, bloks, powers))
