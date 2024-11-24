def generate_string(n):
    vowels = "aeiou"
    result = ""
    for i in range(n):
        result += vowels[i % 5]
    return result

t = int(input())
for _ in range(t):
    n = int(input())
    print(generate_string(n))