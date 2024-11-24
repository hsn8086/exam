from collections import defaultdict
import math

MODULO = 998244353
MAX_N = 200005
MAX_A = 1000005

array_size = 0
numbers = [0] * MAX_N
prime_count = 0
primes = [0] * MAX_A
dp = [0] * MAX_N
sum_values = [0] * MAX_A
is_composite = [False] * MAX_A
prime_factors = defaultdict(list)


def generate_primes():
    global prime_count
    for num in range(2, MAX_A // 2 + 1):
        if not is_composite[num]:
            primes[prime_count] = num
            prime_count += 1
            prime_factors[num].append(num)
        for j in range(prime_count):
            if num * primes[j] >= MAX_A:
                break
            value = num * primes[j]
            is_composite[value] = True
            prime_factors[value] = prime_factors[num][:]
            if num % primes[j] != 0:
                prime_factors[value].append(primes[j])
            else:
                break


def calculate_factors(number):
    factor_count = len(prime_factors[number])
    results = []

    for mask in range(1, 2**factor_count):
        sign = 1 if bin(mask).count("1") % 2 == 1 else -1
        for bit in range(factor_count):
            if mask & (2**bit):
                sign *= prime_factors[number][bit]
        results.append(sign)
    return results


generate_primes()

array_size = int(input().strip())
numbers = list(map(int, input().strip().split()))

for i in range(array_size):
    factors = calculate_factors(numbers[i])

    if i == 0:
        dp[i] = 1
    else:
        for factor in factors:
            abs_factor = abs(factor)
            sign = factor // abs_factor
            dp[i] += sign * sum_values[abs_factor]
            dp[i] %= MODULO

    for factor in factors:
        abs_factor = abs(factor)
        sum_values[abs_factor] += dp[i]
        sum_values[abs_factor] %= MODULO

print(dp[array_size - 1])
