w, h, v = map(int, input().split())
for _ in range(h):
    print("Q" * w)

for _ in range(w):
    print("Q" * (w + v))
