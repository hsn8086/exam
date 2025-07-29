import subprocess
from pathlib import Path
for f in Path("./atcoder-testcases-abc277/abc277/E/in/").iterdir():
    oup=subprocess.run(["pypy3","表_里.py"],text=True,input=f.open("r").read(),capture_output=True)
    print(f.name,"rst:")
    print(oup.stderr,oup.stdout)
