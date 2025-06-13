from typing import Generator, Any


def c(n):
    if n <= 1:
        return n
    else:
        a = yield c(n - 1)
        return a + 1


def event_loop(s: Generator):
    stk, last_rst = [s], None
    while stk:
        try:
            func, last_rst = stk[-1].send(last_rst), None
            stk.append(func)
        except StopIteration as e:
            last_rst = e.value
            stk.pop()
    return last_rst


print(f"Final result: {event_loop(c(1000000))}")
