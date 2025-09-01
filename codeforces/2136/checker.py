import subprocess
import sys


class Interactor:
    def __init__(self):
        from random import randint

        self.init_output = ""
        self.x, self.y = 100, 100
        self.now_x, self.now_y = self.x, self.y
        n = 10
        self.point = [(randint(1, 200), randint(1, 200)) for _ in range(n)]
        self.init_output += "1\n"
        self.init_output += str(n) + "\n"
        for i in range(n):
            self.init_output += "".join(map(str, self.point[i])) + "\n"
        self.init_output.strip()
    def response(self, query: str):
        print(query.split())
        cmd, *args = query.split()
        if cmd == "?":
            mode, k = args
            k = int(k)
            if mode == "R":
                self.now_x += k
            elif mode == "L":
                self.now_x -= k
            elif mode == "U":
                self.now_y += k
            else:
                self.now_y -= k
            ans = 10**18
            for px, py in self.point:
                ans = min(ans, abs(px - self.now_x) + abs(py - self.now_y))
            print(ans)
            return str(ans)

        elif cmd == "!":
            ans_x, ans_y = map(int, args)
            if ans_x == self.x and ans_y == self.y:
                return "Correct"
            else:
                return f"Wrong! The answer is {self.x} {self.y}"

    def start(self, cmd):
        with subprocess.Popen(
            cmd,
            text=True,
            stdin=-1,
            stdout=-1,
        ) as p:
            if self.init_output:
                p.stdin.write(self.init_output + "\n")
                p.stdin.flush()
            while resp := self.response(p.stdout.readline()):
                p.stdin.write(resp + "\n")
                p.stdin.flush()


Interactor().start(["python", "D._For_the_Champion.py"])
