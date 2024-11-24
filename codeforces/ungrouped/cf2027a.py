num_of_tc = int(input())
for _ in range(num_of_tc):
    max_w, max_h = 0, 0
    for _ in range(int(input())):
        w, h = map(int, input().split())
        max_w = max(max_w, w)
        max_h = max(max_h, h)
    print(max_h * 2 + max_w * 2)
