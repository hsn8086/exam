MOD = 10**9 + 7

# def calculate_incorrect_binomials(N):
#     C = [[0 for _ in range(N)] for _ in range(N)]

#     # Initialize base cases
#     for n in range(N):
#         C[n][0] = C[n][n] = 1

#     # Fill the table using the incorrect formula
#     for n in range(2, N):
#         for k in range(1, n):
#             C[n][k] = (C[n][k-1] + C[n-1][k-1]) % MOD

#     return C

# def main():
#     t = int(input())  # Number of test cases

#     # Read all n and k values at once
#     n_values = list(map(int, input().split()))
#     k_values = list(map(int, input().split()))

#     # Assuming the maximum n won't exceed 100000 as per constraints
#     max_n = max(n_values) + 1
#     C = calculate_incorrect_binomials(max_n)

#     # Output results
#     for i in range(t):
#         print(C[n_values[i]][k_values[i]])

# if __name__ == "__main__":
#     main()
t = int(input())  # Number of test cases

# Read all n and k values at once
n_values = list(map(int, input().split()))
k_values = list(map(int, input().split()))
MOD = 10**9 + 7  # 假设这里的MOD是某个常用的质数, 如1000000007

def power(base, exponent, mod):
    result = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        exponent = exponent >> 1  # 右移一位，等价于除以2
        base = (base * base) % mod
    return result

for i in k_values:
    rt = power(2, i, MOD)
    print(rt)