nums = list(map(int, input().split()))
print(sum(nums) * (1 << (len(nums) - 1)))
