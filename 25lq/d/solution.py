def check_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


start = 2024
start_weekday = 0
end = 114514

sum_ = 0
for i in range(start + 1, end + 1):
    sum_ += 365 + int(check_year(i))


a, b = divmod(sum_, 7)
print(a + (1 if b + start_weekday >= 4 else 0))
