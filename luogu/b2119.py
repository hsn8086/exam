def delete(s: str):
    s = s.strip()
    if s.endswith("ly"):
        return s[:-2]
    elif s.endswith("ing"):
        return s[:-3]
    elif s.endswith("er"):
        return s[:-2]
    else:
        return s

inp = input()
print(delete(inp))