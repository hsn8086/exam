import subprocess


class Interactor:
    def __init__(self):
        self.init_output = ""

    def response(self, query: str): ...

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


Interactor().start()

# class Interactor:
#     def __init__(self):

#         # ans=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#         ans = list("ABCDEF")
#         self.lmt = 15
#         shuffle(ans)
#         self.ans = "".join(ans)
#         self.cnt = 0

#         self.init_output = str(len(self.ans)) + " " + str(self.lmt)
#     def response(self, query: str):
#         if query.startswith("!"):
#             _, rst = query.split()
#             if rst == self.ans:
#                 print(True)
#             else:
#                 print(rst, self.ans, sep="\n")
#                 raise
#             return
#         self.cnt += 1
#         if self.cnt > self.lmt:
#             raise
#         _, f, s = query.split()
#         sy = ">" if self.ans.index(f) > self.ans.index(s) else "<"
#         return sy

#     def start(self):
#         with subprocess.Popen(
#             ["python3", "B_Interactive_Sorting.py"],
#             text=True,
#             stdin=-1,
#             stdout=-1,
#             stderr=-1,
#         ) as p:
#             if self.init_output:
#                 p.stdin.write(self.init_output + "\n")
#                 p.stdin.flush()
#             while line := p.stdout.readline():
#                 if resp := self.response(line):
#                     p.stdin.write(resp + "\n")
#                     p.stdin.flush()
#                 else:
#                     break

# Interactor().start()
