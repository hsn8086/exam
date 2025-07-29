from collections import defaultdict
from typing import Generator, Any


def event_loop(start_gen: Generator):
    stack: list[Generator] = [start_gen]

    last_result: Any = None

    while stack:
        now_task = stack[-1]
        try:
            next_val = now_task.send(last_result)

            last_result = None

            if isinstance(next_val, Generator):
                stack.append(next_val)
            else:
                last_result = next_val
                stack.pop()

        except StopIteration as e:
            stack.pop()

            last_result = e.value

        except TypeError as e:
            if (
                last_result is None
                and "can't send non-None value to a just-started generator"
                not in str(e)
            ):
                last_result = None
                continue
            else:
                raise e

    return last_result


def clac(a: list, p: int, e: dict):
    if len(e[p]) == 0:
        yield a[p - 1]
        return
    m = float("+inf")
    for i in e[p]:
        v = yield clac(a, i, e)
        m = min(v, m)
    if m < a[p - 1]:
        yield m
        return
    v = (a[p - 1] + m) // 2
    a[p - 1] = v
    yield v


for _ in range(int(input())):
    n = input()
    a = list(map(int, input().split()))
    fat = list(map(int, input().split()))

    e = defaultdict(list)
    for i, f in enumerate(fat):
        e[f].append(i + 2)
    # print(a)
    m = float("inf")
    for i in e[1]:
        m = min(event_loop(clac(a, i, e)), m)
    # print(a)
    # print(e)
    print(m + a[0])
