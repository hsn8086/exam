from pathlib import Path
import json

with Path("problem.json").open("r") as f:
    rule = json.load(f)

pre_v = {}
for line in rule["pre"]:
    exec(line, pre_v)
for i, v in enumerate(rule["examples"]):
    v.update(pre_v)
    for line in rule["template"]:
        try:
            print(str(eval(line, v)).strip())
        except Exception as e:
            print(f"Error in line {i+1}: {e}")
            print(f"Variables: {v}")
            print(f"Line: {line}")
            exit(1)
