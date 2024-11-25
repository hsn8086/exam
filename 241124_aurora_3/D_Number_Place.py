def cell(matrix,x_,y_):
    cheacker=[False]*10
    for y in range(3):
        for x in range(3):
            v=matrix[x+x_][y+y_]
            if cheacker[v]:
                return False
            cheacker[v]=True
    return True

def solve(matrix):
    
    for x in range(9):
        cheacker=[False]*10
        for y in range(9):
            v=matrix[x][y]
            if cheacker[v]:
                return "No"
            cheacker[v]=True

    for y in range(9):
        cheacker=[False]*10
        for x in range(9):
            v=matrix[x][y]
            if cheacker[v]:
                return "No"
            cheacker[v]=True
    for x in range(3):
        for y in range(3):
            if not cell(matrix,x*3,y*3):
                return "No"
    return "Yes"
matrix=[]
for _ in range(9):
    matrix.append(list(map(int,input().split())))
print(solve(matrix))
