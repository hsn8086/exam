from collections import Counter

for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    cnt = Counter(s)
    max_count = max(cnt.values())
    total_needed = 3 * max_count
    current_total = n
    operations_needed = total_needed - current_total
    if operations_needed > 2 * n:
        print(-1)
        continue

    required = {char: max_count - cnt[char] for char in ["L", "I", "T"]}

    possible = True
    for char in required:
        if required[char] < 0:
            possible = False
    if not possible:
        print(-1)
        continue

    operations = []
    current_s = list(s)
    remaining = required.copy()

    while sum(remaining.values()) > 0:
        inserted = False
        for i in range(len(current_s) - 1):
            if current_s[i] != current_s[i + 1]:
                available_chars = {"L", "I", "T"} - {current_s[i], current_s[i + 1]}

                for char in available_chars:
                    if remaining[char] > 0:
                        operations.append(i + 1)
                        current_s.insert(i + 1, char)
                        remaining[char] -= 1
                        inserted = True
                        break
                if inserted:
                    break
        if not inserted:
            possible = False
            break

    if not possible:
        print(-1)
    else:
        print(len(operations))
        for op in operations:
            print(op)
