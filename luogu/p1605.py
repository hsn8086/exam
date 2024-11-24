n,m,t=map(int,input().split())
sx,sy,fx,fy=map(int,input().split())
blocks=set()

for i in range(t):
    x,y=map(int,input().split())
    blocks.add((x,y))

def dfs(x,y,n,m,visited:set):
    if x>n or y>m or x<1 or y<1:
        return 0
    if (x,y) in blocks:
        return 0
    if (x,y) in visited:
        return 0
    if x==fx and y==fy:
        return 1
        
    visited.add((x,y))
    total = sum([
        dfs(x+1,y,n,m,visited),
        dfs(x-1,y,n,m,visited),
        dfs(x,y+1,n,m,visited),
        dfs(x,y-1,n,m,visited)
    ])
    visited.remove((x,y)) 
    return total

visited = set()
print(dfs(sx,sy,n,m,visited))