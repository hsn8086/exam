for _ in range(int(input())):
    x, y = map(int, input().split())
    matrix = []
    for _ in range(x):
        matrix.append(str(input()))
    xor_1 = 0
    for i in matrix:
        xor_1 ^= int(i, 2)

    xor_2 = 0
    for i in zip(*matrix):
        xor_2 ^= int("".join(i), 2)

    print(max(xor_1.bit_count(), xor_2.bit_count()))
