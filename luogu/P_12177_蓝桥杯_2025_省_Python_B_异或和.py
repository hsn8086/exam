n = int(input())
a = list(map(int, input().split()))
print(sum(sum((a[i] ^ a[j]) * (j - i) for j in range(i + 1, n)) for i in range(n - 1)))
