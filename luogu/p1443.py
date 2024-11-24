from collections import deque

def is_valid(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


directions = [
    (-2,-1), (-2,1), (2,-1), (2,1),
    (-1,-2), (-1,2), (1,-2), (1,2)
]

n, m, x, y = map(int, input().split())
x -= 1 
y -= 1


min_step = [[-1] * m for _ in range(n)]
queue = deque([(x, y, 0)])
min_step[x][y] = 0


while queue:
    curr_x, curr_y, steps = queue.popleft()
    
    for dx, dy in directions:
        new_x, new_y = curr_x + dx, curr_y + dy
        if is_valid(new_x, new_y, n, m) and min_step[new_x][new_y] == -1:
            min_step[new_x][new_y] = steps + 1
            queue.append((new_x, new_y, steps + 1))

for row in min_step:
    print(*row)