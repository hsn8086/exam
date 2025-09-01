s = input().strip()

if s.endswith(("er", "ly")):
    print(s[:-2])
elif s.endswith("ing"):
    print(s[:-3])
else:
    print(s)
