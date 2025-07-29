import subprocess
for i in range(100):
    data=subprocess.run(["python3", "c2_gen.py"], stdout=subprocess.PIPE, text=True)
    # print("next")
    res=subprocess.run(["python3", "A_Adjacent_Delete.py"], input=data.stdout, text=True,capture_output=True)
    print(res.stdout)