from itertools import  product
n=int(input())
matrix=[]
for _ in range(n):
    matrix.append(list(map(int,input().split())))

def fill(matrix,x,y,n,flag,judge=0,visited=set()):
    if (x,y) in visited:
        return
    visited.add((x,y))
    if x>=n or y>=n or x<0 or y<0:
        return
    if matrix[x][y]!=judge:
        return
    matrix[x][y]=flag
    fill(matrix,x+1,y,n,flag,judge,visited)
    fill(matrix,x-1,y,n,flag,judge,visited)
    fill(matrix,x,y+1,n,flag,judge,visited)
    fill(matrix,x,y-1,n,flag,judge,visited)

def check_open(matrix,x,y,n,flag=0,visited=set()):
    if (x,y) in visited:
        return False
    visited.add((x,y))
    
    if x>=n or y>=n or x<0 or y<0:
        return True
    if matrix[x][y]!=flag:
        return False
    
    return any([
        check_open(matrix,x+1,y,n,flag,visited),
        check_open(matrix,x-1,y,n,flag,visited),
        check_open(matrix,x,y+1,n,flag,visited),
        check_open(matrix,x,y-1,n,flag,visited)
    ])

for x,y in product(range(n),repeat=2):
    if matrix[x][y]==0:
        flag=3 if check_open(matrix,x,y,n) else 2
        fill(matrix,x,y,n,flag,0)


for row in matrix:
    print(*map(lambda x: 0 if x==3 else x,row))