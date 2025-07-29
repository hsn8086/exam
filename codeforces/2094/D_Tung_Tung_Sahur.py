for _ in range(int(input())):
    p = input()
    s = input()
    i = j = 0
    while i < len(p) and j < len(s):
        if p[i] == s[j]:
            if j + 1 < len(s) and s[j + 1] == s[j]:
                j += 2
            else:
                j += 1
            i += 1
        else:
            print("NO")
            break
    else:
        print("YES" if i == len(p) and j == len(s) else "NO")
