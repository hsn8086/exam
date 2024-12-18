import sys
import math


def mx(num):
    return math.factorial(num)


def kth_permutation(n, k):
    numbers = list(range(1, n + 1))
    permutation = []
    k -= 1  # Convert to 0-based index
    while n > 0:
        fact = math.factorial(n - 1)
        index = k // fact
        if index >= len(numbers):
            return -1
        permutation.append(numbers.pop(index))
        k %= fact
        n -= 1
    return permutation


def main():
    import sys

    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    ptr = 1
    for _ in range(t):
        n, k = int(data[ptr]), int(data[ptr + 1])
        ptr += 2
        total = mx(n)
        if k > total:
            print(-1)
        else:
            perm = kth_permutation(n, k)
            if perm == -1:
                print(-1)
            else:
                print(" ".join(map(str, perm)) + " ")


if __name__ == "__main__":
    main()
