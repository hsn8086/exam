import bisect

n, q = map(int, input().split())
scores = list(map(int, input().split()))
queries = [int(input()) for _ in range(q)]

scores.sort()

for q in queries:
    print(n - bisect.bisect_left(scores, q))
