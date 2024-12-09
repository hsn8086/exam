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
        stack = [(self, False)]
        while stack:
            node, visited_children = stack.pop()
            if visited_children:
                q = []
                max_ = 0
                for child in node.nodes:
                    max_road = child.max_road + child.d
                    heapq.heappush(q, max_road)
                    if len(q) > 2:
                        heapq.heappop(q)
                    max_ = max(max_, child.max)
                node.max_branch = sum(q)
                node.max = max(node.max_branch, max_)
                node.max_road = max(q) if q else 0
            else:
                stack.append((node, True))
                for child in node.nodes:
                    stack.append((child, False))
        return self.max


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
                    a = b
                child_node = Node(a, c)
                node.add(child_node)
                queue.append(child_node)
                pop_lst.append(i)
        for offset, idx in enumerate(pop_lst):
            road_lst.pop(idx - offset)

max_d = palace.clac_max()
_sum = 0
for x in range(1, max_d + 1):
    _sum += x + 10

print(_sum)