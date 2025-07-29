from collections.abc import Generator
import sys


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


# Example
inp = chunk_reader(chunk_size=1 << 18)
n, m = map(int, input().split())
a = list(next(inp) for i in range(n))

for _ in range(m):
    print(a[next(inp) - 1])
