t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    from collections import Counter

    count = Counter(a)
    unique_numbers = sorted(count.keys())
    counts = [count[num] for num in unique_numbers]
    
    l = 0
    sum_counts = 0
    max_counts = 0
    for r in range(len(unique_numbers)):
        sum_counts += counts[r]
        while unique_numbers[r] - unique_numbers[l] > r - l:
            sum_counts -= counts[l]
            l += 1
        if r - l + 1 <= k:
            max_counts = max(max_counts, sum_counts)
        else:
            sum_counts -= counts[l]
            l +=1
    print(max_counts)