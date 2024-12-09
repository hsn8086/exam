# import hashlib
# import random
# from rich.progress import track

# last = None
# dig = random.randbytes(32)
# def rod():
#     while True:
#         yield

# for i in track(rod()):
#     hash_ = hashlib.md5(dig,usedforsecurity=False)
#     dig = hash_.hexdigest().encode()
#     if last == dig:
#         break
#     last = dig

# print(dig)
# print(hash_.hexdigest())
import hashlib
import random
from rich.progress import track

last = None


def rod():
    while True:
        yield


rec = set()
while True:
    del rec
    rec = set()
    dig = random.randbytes(32)
    for i in track(range(10**8)):
        hash_ = hashlib.md5(dig, usedforsecurity=False)
        dig = hash_.hexdigest().encode()
        if dig in rec:
            print(hash_.hexdigest())
            break
        rec.add(dig)
    else:
        continue
    break
print(dig)
print(hash_.hexdigest())
