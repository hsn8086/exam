
import tempfile
# import psutil
import time
from typing import Literal
from subprocess import Popen
from typing import Callable
from dataclasses import dataclass


@dataclass
class Result:
    type: Literal[
        "success", "runtime_error", "compile_error", "timeout", "memory_limit_exceeded"
    ]
    output: str = ""
    time: float = 0
    memory: float = 0


@dataclass
class RunProcessResult:
    stdout: str
    stderr: str
    time: float
    memory: float
    status: Literal[
        "success", "runtime_error", "compile_error", "timeout", "memory_limit_exceeded"
    ] = "success"


def run_p(cmd: list, inp: str = "", *, memory_limit: int = 256, timeout: int = 1):
    with Popen(
        cmd, text=True, stdin=-1, stdout=-1, stderr=-1
    ) as p:  # set stdin to -1 for input and stdout stderr to -1 for capture output.
        start = time.time()
        assert p.stdin is not None
        assert p.stdout is not None
        assert p.stderr is not None
        p.stdin.write(inp)
        p.stdin.flush()  # input and flush the buffer
        max_memory = 0
        while True:
            state = p.poll()  # check process state
            if state is not None:
                return RunProcessResult(
                    stdout=p.stdout.read(),
                    stderr=p.stderr.read(),
                    time=time.time() - start,
                    memory=max_memory,
                )

            # child_process = psutil.Process(
            #     p.pid
            # )  # use psutil tu monitoring process status

            # mem_use = child_process.memory_full_info().uss / (1024**2)
            # max_memory = max(max_memory, mem_use)
            # if mem_use > memory_limit:  # check memory
            #     child_process.kill()
            #     child_process.terminate()
            #     return RunProcessResult(
            #         status="memory_limit_exceeded",
            #         stdout=p.stdout.read(),
            #         stderr=p.stderr.read(),
            #         time=time.time() - start,
            #         memory=max_memory,
            #     )

            if time.time() - start >= timeout:  # check timeout
                p.kill()
                p.terminate()
                # child_process.kill()
                # child_process.terminate()
                return RunProcessResult(
                    status="timeout",
                    stdout=p.stdout.read(),
                    stderr=p.stderr.read(),
                    time=time.time() - start,
                    memory=max_memory,
                )


def run(
    code: str,
    inp: str,
    cmd: str,
    *,
    memory_limit: int = 256,
    timeout: int = 1,
    compile_func: Callable | None = None,
) -> Result:
    with tempfile.NamedTemporaryFile() as tmp:
        tmp.write(code.encode())
        tmp.seek(0)
        # print(f"python{version}", tmp.name)
        file_name = tmp.name
        if compile_func:
            try:
                file_name = compile_func(file_name)
            except Exception as e:
                return Result(output=str(e), type="compile_error", time=0, memory=0)
        try:
            rst = run_p(
                cmd.format(file_name=file_name).split(),
                inp=inp,
                timeout=timeout,
                memory_limit=memory_limit,
            )
            stdout = rst.stdout
            stderr = rst.stderr
            time = rst.time
            memory = rst.memory
            status = rst.status
        except Exception as e:
            return Result(output=str(e), type="runtime_error", time=0, memory=0)
        if status == "timeout":
            return Result(output=stdout, type="timeout", time=time, memory=memory)
        elif status == "memory_limit_exceeded":
            return Result(
                output=stdout, type="memory_limit_exceeded", time=time, memory=memory
            )

        if stderr:
            return Result(output=stderr, type="runtime_error", time=time, memory=memory)
        return Result(output=stdout, type="success", time=time, memory=memory)


def py(
    code: str,
    inp: str,
    *,
    memory_limit: int = 256,
    timeout: int = 1,
    version: str = "3",
) -> dict:
    return run(
        code=code,
        inp=inp,
        cmd=f"python{version} {{file_name}}",
        memory_limit=memory_limit,
        timeout=timeout,
    ).__dict__


print(py("print('hello world')", ""))
