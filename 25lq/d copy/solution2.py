import time
from datetime import datetime

now = time.time() + 86400
ds = ""
count = 0
count2 = 0
while ds != "3456-11-27":
    now += 86400
    d = datetime.fromtimestamp(now)
    ds = d.strftime("%Y-%m-%d")
    if d.weekday() == 3:
        count += 1
    count2 += 1
print(count, count2)
