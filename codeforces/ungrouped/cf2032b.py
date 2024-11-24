def solve(n, k):
    if n == 1:
        if k == 1:
            return "1\n1"
        else:
            return "-1"

    if k == 1 or k == n:
        return "-1"
    if k%2==0:
        return f"3\n1 {k} {k + 1}"
    else:
        return f"3\n1 {k-1} {k+2}"

num_of_tc = int(input())
for _ in range(num_of_tc):
    n, k = map(int, input().split())
    print(solve(n,k))