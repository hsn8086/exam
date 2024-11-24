def pair(s:str):
    for i in s:
        if i=="A":
            yield "T"
        elif i=="T":
            yield "A"
        elif i=="C":
            yield "G"
        elif i=="G":
            yield "C"

inp=input()
print("".join(pair(inp)))
