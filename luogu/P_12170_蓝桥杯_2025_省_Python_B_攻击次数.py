init = 2025
round_ = 0
while True:
    round_ += 1
    a = 5
    if round_ % 2 == 0:
        b = 2
    else:
        b = 15

    if round_ % 3 == 1:
        c = 2
    elif round_ % 3 == 2:
        c = 10
    else:
        c = 7
    init -= a + b + c
    if init <= 0:
        print(round_)
        break
