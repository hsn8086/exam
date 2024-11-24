n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
s = set()

for num in a:
    if num % k != 0 or (num // k) not in s:
        s.add(num)

print(len(s))
