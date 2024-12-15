submit = int(input())
fir_gt = 0
charge = 0
for _ in range(submit):
    tim, status = map(int, input().split())
    if status:
        fir_gt += tim
    if status == 0:
        charge += 20
print(fir_gt + charge)
