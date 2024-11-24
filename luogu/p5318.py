n,m=map(int,input().split())
graph=[[0 for i in range(n)] for i in range(n)]
for _ in range(m):
    x,y=map(int,input().split())
    graph[x][y]=1

def dfs(gra,node,visited):
    if node==0:
        return
    if node not in visited:
        visited.append(node)
    for i in gra[node]:
        dfs(gra,i,visited)
visited=[]
dfs(graph,1,visited)
print(visited)