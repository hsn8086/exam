def mapping(num):
    if num < 10:
        return str(num)
    return chr(num - 10 + ord('A'))
def to_x(num: int, x: int):
    stack = []
    while num:
        stack.append(mapping(num % x))
        num //= x
    return "".join(stack[::-1]) if stack else "0"


num = int(input())
x = int(input())

print(to_x(num, x))
