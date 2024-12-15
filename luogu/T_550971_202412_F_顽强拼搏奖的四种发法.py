n, t, p, k = map(int, input().split())
sol = [set() for _ in range(t + 1)]

submit = [tuple(map(int, input().split())) for i in range(n)]

for tid, pid, state in submit:
    if state:
        sol[tid].add(pid)

award1 = -1
for tid, pid, state in reversed(submit):
    if state:
        award1 = tid
        break

award2 = -1
solat = [set() for _ in range(t + 1)]
for tid, pid, state in submit:
    if state:
        if pid not in solat[tid]:
            solat[tid].add(pid)
            award2 = tid

award3 = -1
solat = [set() for _ in range(t + 1)]
for tid, pid, state in submit:
    if state and pid not in solat[tid]:
        solat[tid].add(pid)
        if len(sol[tid]) < k:
            award3 = tid

award4 = -1
solat = [set() for _ in range(t + 1)]
for tid, pid, state in submit:
    if state and not len(solat[tid]):
        solat[tid].add(pid)
        award4 = tid

print(award1, award2, award3, award4)
