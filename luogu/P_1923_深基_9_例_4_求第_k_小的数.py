from collections.abc import Generator
import sys
import random


def chunk_reader(func=int, chunk_size=1 << 15) -> Generator[int, None, None]:
    inp_cache = ""
    while True:
        chunk = sys.stdin.read(chunk_size)  # 读入一块
        if not chunk:  # 判断是否为结尾
            if inp_cache:  # 判断缓存内是否还有内容
                yield func(inp_cache)  # 输出
                del inp_cache  # 删除缓存
            break  # 跳出循环

        for c in chunk:
            if c.isspace():  # 判断当前字符是否是空格或者换行
                if inp_cache:  # 如果当前缓存有内容, 即代表此内容已经到了结尾
                    yield func(inp_cache)  # 输出
                    del inp_cache
                    inp_cache = ""  # 删除缓存并重新初始化
            else:
                inp_cache += c  # 否则把字符串加入缓存
            del c  # 删除字符
        del chunk  # 删除区块


def quick_sel(arr, k):
    l, r = 0, len(arr) - 1
    while l <= r:
        pivot_idx = random.randint(l, r)
        arr[l], arr[pivot_idx] = arr[pivot_idx], arr[l]
        pivot = arr[l]
        i = l + 1
        for j in range(l + 1, r + 1):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[l], arr[i - 1] = arr[i - 1], arr[l]
        if k == i - 1:
            return arr[i - 1]
        elif k < i - 1:
            r = i - 2
        else:
            l = i
    return -1


inp = chunk_reader(chunk_size=1 << 18)
n, k = next(inp), next(inp)
a = [next(inp) for _ in range(n)]
print(quick_sel(a, k))
