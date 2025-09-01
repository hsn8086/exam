from pathlib import Path
import sys


def query(mode: str, k: int) -> int:
    """向裁判机发出询问：从当前位置移动 mode 方向 k 步，返回最小曼哈顿距离"""
    print(f"? {mode} {k}", flush=True)
    return int(input())


def answer(x: int, y: int):
    """提交答案"""
    print(f"! {x} {y}", flush=True)


for _ in range(int(input())):
    n = int(input())
    # 读入锚点（交互题里通常不会直接给，这里是本地调试）
    points = [tuple(map(int, input().split())) for _ in range(n)]

    M = 10**9

    # 四个大方向各测一次
    dR = query("R", M)
    dL = query("L", M)
    dU = query("U", M)
    dD = query("D", M)

    # 由公式：
    # dR = M - x* + |Y-y*|
    # dL = M + x* + |Y-y*|
    # 相减可得: x* = (dL - dR) // 2
    # 同理: y* = (dD - dU) // 2
    x = (dL - dR) // 2
    y = (dD - dU) // 2

    # 输出答案
    answer(x, y)
    Path.cwd() / "D._For_the_Champion.txt".write_text(sys.stdin.readline())
