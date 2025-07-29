import sys
from functools import cmp_to_key
flush = sys.stdin.flush


def query(a, b):
    print(f"? {a} {b}")
    flush()
    rst=input() == "<"

    return -100 if rst else 100


def ans(lst: list):
    print("!", " ", *lst, sep="")

n,q=map(int, input().split())

lst=list(map(chr,range(65,65+n)))
lst.sort(key=cmp_to_key(query))
ans(lst)