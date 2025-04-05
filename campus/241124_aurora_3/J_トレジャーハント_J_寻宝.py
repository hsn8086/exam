from collections import defaultdict, deque
from dataclasses import dataclass
from typing import Dict, Set

@dataclass
class Road:
    __slots__ = ['to', 'time']
    to: int
    time: int

@dataclass
class Task:
    __slots__ = ['now', 'used_time', 'bonce']
    now: int
    used_time: int
    bonce: int

n, m, t = map(int, input().split())
town_lst = [0] + list(map(int, input().split()))
roads: Dict[int, list[Road]] = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, input().split())
    roads[a].append(Road(to=b, time=c))

max_bonce = 0


queue: deque[Task] = deque([Task(now=1, used_time=0, bonce=0)])
while queue:
    task = queue.popleft()
    state = (task.now, task.used_time)
    
    if task.used_time >= t:
        continue

    max_bonce = max(max_bonce, task.bonce)

    # stay
    queue.append(
        Task(
            now=task.now,
            used_time=task.used_time + 1,
            bonce=task.bonce + town_lst[task.now],
        )
    )

    # leave
    for road in roads[task.now]:
        print(road)
        if task.used_time + road.time < t:
            queue.append(
                Task(now=road.to, used_time=task.used_time + road.time, bonce=task.bonce)
            )
print(max_bonce)
