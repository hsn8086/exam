import json
from pathlib import Path
import subprocess
import time
import shutil
import zipfile

with Path("problem.json").open("r") as f:
    rule = json.load(f)

def data_gen(name: str, v: dict):
    fp_in = p / (name + ".in")
    fp_out = p / (name + ".out")
    
    with fp_in.open("w") as f:
        for line in rule["template"]:
            f.write(str(eval(line, v)).strip() + "\n")

    with fp_in.open("r") as fin, fp_out.open("w") as fout:
        start = time.time()
        sp = subprocess.run(rule["solution"], stdin=fin, text=True, capture_output=True)
        used = time.time() - start
        if used > rule["time_limit"] / 1000:
            print(f"Test {name} failed: time limit exceeded")
            print(f"Time: {used}")
            raise TimeoutError()
        fout.write(sp.stdout)


p = Path("data")
shutil.rmtree(p, ignore_errors=True)
p.mkdir(exist_ok=True)

test_zip = Path("tests.zip")
if test_zip.exists():
    test_zip.unlink()

example_zip = Path("examples.zip")
if example_zip.exists():
    example_zip.unlink()

pre_v={}
for line in rule["pre"]:
        exec(line, pre_v)
with zipfile.ZipFile(test_zip, "w") as z:
    for i, v in enumerate(rule["tests"]):
        v.update(pre_v)
        data_gen(f"{i+1}", v)
        z.write(p / f"{i+1}.in", f"{i+1}.in")
        z.write(p / f"{i+1}.out", f"{i+1}.out")

with zipfile.ZipFile(example_zip, "w") as z:
    for i, v in enumerate(rule["examples"]):
        v.update(pre_v)
        data_gen(f"ex{i+1}", v)
        z.write(p / f"ex{i+1}.in", f"ex{i+1}.in")
        z.write(p / f"ex{i+1}.out", f"ex{i+1}.out")
