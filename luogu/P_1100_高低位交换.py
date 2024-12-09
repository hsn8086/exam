mask_1 = 0xFFFF0000
mask_2 = 0x0000FFFF
num = int(input())
high = num & mask_1
low = num & mask_2
high >>= 16
low <<= 16
result = high | low
print(result)
