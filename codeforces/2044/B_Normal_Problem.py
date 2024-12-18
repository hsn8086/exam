ntc = int(input())
for _ in range(ntc):
    a = input().strip()
    char_map = {"p": "q", "q": "p", "w": "w"}
    print("".join(char_map[c] for c in reversed(a)))
