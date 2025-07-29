import random
import subprocess
import time
for i in range(1,100000,500):
    print(1)
    for _ in range(1):
        
        txt=f"1\n{i}\n"
        a=list(range(1,i+1))
        random.shuffle(a)
        txt+=' '.join(map(str,a))
        random.shuffle(a)
        txt+=' '.join(map(str,a))
        start=time.time()
        # 使用 subprocess 运行 Python 文件并通过标准输入传递文本
        process = subprocess.Popen(
            ["python", "C_Disappearing_Permutation.py"],  # 如果是 Python 3，可能需要改为 "python3"
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True  # Python 3.7+ 可用，否则使用 universal_newlines=True
        )

        # 向进程发送输入文本并获取输出
        stdout, stderr = process.communicate(input=txt)
        if time.time()-start>1:
            raise