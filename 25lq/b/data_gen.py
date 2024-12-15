from pathlib import Path
import subprocess
import time
import shutil

rule = {
    "template": [
        "f'{n} {m}'",
        "' '.join(str(random.randint(0,end)) for _ in range(n))",
    ],
    "pre": [
        "import random",
    ],
    "solution": ["python", "solution.py"],
    "time_limit": 2000,
    "memory_limit": 256 * 1024,
    "examples": [
        {"n": 3, "m": 1, "end": 10},
        {"n": 5, "m": 2, "end": 20},
        {"n": 10, "m": 3, "end": 100},
    ],
    "tests": [
        {"n": 10, "m": 2, "end": 10**2},
        {"n": 10**2, "m": 2, "end": 10**5},
        {"n": 10**2, "m": 10, "end": 10**5},
        {"n": 10**2, "m": 10, "end": 10**9},
        {"n": 10**5, "m": 10, "end": 10**9},
        {"n": 10**5, "m": 2 * 10, "end": 10**9},
        {"n": 10**5, "m": 10**2, "end": 10**9},
        {"n": 10**6, "m": 10, "end": 10**9},
        {"n": 10**6, "m": 10**2, "end": 10**9},
        {"n": 10**6, "m": 10**3, "end": 10**9},
    ],
}


def data_gen(name: str, v: dict):
    fp_in = p / (name + ".in")
    fp_out = p / (name + ".out")
    for line in rule["pre"]:
        exec(line, v)

    with fp_in.open("w") as f:
        for line in rule["template"]:
            f.write(str(eval(line, v)).strip() + "\n")

    with fp_in.open("r") as fin, fp_out.open("w") as fout:
        start = time.time()
        sp = subprocess.run(rule["solution"], stdin=fin, text=True, capture_output=True)
        used = time.time() - start
        if used > rule["time_limit"] / 1000:
            print(f"Test {i+1} failed: time limit exceeded")
            print(f"Expected: {sp.stdout}")
            print(f"Time: {used}")
            raise TimeoutError()
        fout.write(sp.stdout)


p = Path("data")
shutil.rmtree(p, ignore_errors=True)
p.mkdir(exist_ok=True)

for i, v in enumerate(rule["tests"]):
    data_gen(f"{i+1}", v)
for i, v in enumerate(rule["examples"]):
    data_gen(f"ex{i+1}", v)
