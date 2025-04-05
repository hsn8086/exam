n = int(input())
s = input()
for i in range(1, n):
    if s[i - 1] == "a" and s[i] == "b" or s[i - 1] == "b" and s[i] == "a":
        print("Yes")
        break
else:
    print("No")
