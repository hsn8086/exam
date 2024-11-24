stack = []
inp = input()
temp = ""
for i in inp:
    if i == ".":
        stack.append(int(temp))
        temp = ""
    elif i == "/":
        b, a = stack.pop(), stack.pop()
        stack.append(a // b)
    elif i == "*":
        a, b = stack.pop(), stack.pop()
        stack.append(a * b)
    elif i == "-":
        b, a = stack.pop(), stack.pop()
        stack.append(a - b)
    elif i == "+":
        a, b = stack.pop(), stack.pop()
        stack.append(a + b)
    elif i=="@":
        print(stack[0])
    else:
        temp += i


