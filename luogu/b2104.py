n,m=map(int,input().split())
matrix_a=[]
matrix_b=[]
for i in range(n):
    matrix_a.append(list(map(int,input().split())))

for i in range(n):
    matrix_b.append(list(map(int,input().split())))

for a_lst,b_lst in zip(matrix_a,matrix_b):
    print(" ".join(str(a+b) for a,b in zip(a_lst,b_lst)))
