from typing import Literal
from pathlib import Path
from threading import Thread, Lock


def req(code_type: Literal["py", "pypy"], code: str, inp: str):
    import httpx
    import json

    # url="192.168.49.2:30000"
    url = "127.0.0.1:8000"
    resp = httpx.post(
        f"http://{url}/api/v1/runner/" + code_type,
        json=dict(code=code, input=inp),
    )
    # print(resp.text)
    rst_resp = httpx.get(
        f"http://{url}/api/v1/runner/get_result?task_id={resp.json()}", timeout=10
    )
    try:
        return rst_resp.json()
    except json.decoder.JSONDecodeError:
        raise RuntimeError(rst_resp.text)


def req_and_save(code_type: Literal["py", "pypy"], code: str, inp: str):
    rsp = req(code_type=code_type, code=code, inp=inp)
    with lock:
        rst.append(rsp)


base_p = Path("checkpoint/简易计算器")
p = base_p / "data"
code = (base_p / "main.py").read_text()
lock = Lock()

for j in ["py", "pypy"]:
    ts = []
    rst = []
    print(f"Running by {j}:")
    for f in p.iterdir():
        if f.suffix == ".in":
            t = Thread(target=req_and_save, args=(j, code, f.read_text()))
            t.start()
            ts.append(t)

    for t in ts:
        t.join()

    for i in rst:
        print(f"{int(i['time'] * 1000)}ms", f"{i['memory']:.2f}", "status:", i["type"])
