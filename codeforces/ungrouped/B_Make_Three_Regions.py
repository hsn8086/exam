
for _ in range(int(input())):
    matrix=[]
    n=int(input())
    for _ in range(2):
        matrix.append(input())
    cnt=0
    for i in range(1,n-1):

        if matrix[0][i]==matrix[0][i+1]==matrix[0][i-1]==matrix[1][i]=="." and matrix[1][i-1]==matrix[1][i+1]=="x":
            cnt+=1
        if matrix[1][i]==matrix[1][i+1]==matrix[1][i-1]==matrix[0][i]=="." and matrix[0][i-1]==matrix[0][i+1]=="x":
            cnt+=1   
    print(cnt)