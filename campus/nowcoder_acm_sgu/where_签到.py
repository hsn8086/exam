x, y, z = map(int, input().split())
# right_p = 0
# # case has
# has_p = z / x
# # case has and check
# right_p += has_p * min(1, (y / z) if z else float("+inf"))


# # case havent
# hav_p = 1 - has_p
# right_p += hav_p * min(1, (y / (x - z)) if (x - z) else float("+inf"))

# print(right_p)
# right = 0
# if y >= z:
#     # know ans
#     right += z / x
#     right += (1 - z / x) * (y / (x - z))
# else:
#     right += (z / x) * (y / z)
#     right += (1 - z / x) * (y / (x - z))
# print(right)

right = 0
# print(((x + z - y) / x))
# print(y / x + y / (z * x))

# print((y / x) ** 2 + (1 - (y / x)) * (1 - (z / (x - y))) * (y / x))
