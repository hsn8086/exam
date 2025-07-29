from collections import deque
import heapq


class Node:
    def __init__(self, num: int, d=0):
        self.id = num
        self.nodes: list[Node] = []
        self.d = d
        self.max_road = 0
        self.max = 0
        self.max_branch = 0

    def add(self, node: "Node"):
        self.nodes.append(node)

    def clac_max(self):
        if self.max:
            return self.max
        max_ = self.clac_max_branch()
        for node in self.nodes:
            max_ = max(max_, node.clac_max())
        self.max = max_
        return max_

    def clac_max_branch(self):
        if self.max_branch:
            return self.max_branch
        q = []
        heapq.heappush(q, 0)
        for node in self.nodes:
            if len(q) == 2:
                heapq.heappushpop(q, node.d + node.clac_max_road())
            else:
                heapq.heappush(q, node.d + node.clac_max_road())
        self.max_branch = sum(q)
        return self.max_branch

    def clac_max_road(self):
        if self.max_road:
            return self.max_road

        max_ = 0
        for node in self.nodes:
            temp = yield node.clac_max_road
            max_ = max(max_, node.d + temp)
        self.max_road = max_
        return max_


n = int(input())
palace = Node(1)
road_lst = []
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    if a == 1 or b == 1:
        if a == 1:
            a = b
        palace.add(Node(a, c))
    else:
        road_lst.append((a, b, c))

queue = deque()
queue.append(palace)
while road_lst:
    task: Node = queue.popleft()
    for node in task.nodes:
        node: Node
        pop_lst = []
        for i in range(len(road_lst)):
            a, b, c = road_lst[i]
            if a == node.id or b == node.id:
                if a == node.id:
                    a == b
                node.add(Node(a, c))
                pop_lst.append(i)
        for offset, idx in enumerate(pop_lst):
            road_lst.pop(idx - offset)

max_d = 0

_sum = 0
for x in range(1, max_d + 1):
    _sum += x + 10

print(_sum)
