import subprocess
data=subprocess.run(["python3", "c2_gen.py"], stdout=subprocess.PIPE, text=True)
print("next")
res=subprocess.run(["python3", "C_2_Skibidus_and_Fanum_Tax_hard_version.py"], input=data.stdout, text=True)


print(res.stdout)