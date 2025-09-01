
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


for _ in range(int(input())):
    print(fib(int(input())))
