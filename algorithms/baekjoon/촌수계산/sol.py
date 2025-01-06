n = int(input())
a, b = map(int, input().split())
m = int(input())

matrix = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    matrix[x].append(y)
    matrix[y].append(x)

visited = [False]*(n+1)
result = []

def dfs(v, num):
    num += 1 # 촌수 1 증가
    visited[v] = True # 현재 노드 방문 처리
    
    if v == b:
        result.append(num)
    
    for i in matrix[v]:
        if not visited[i]:
            dfs(i, num)
            
dfs(a, 0)

if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)

"""
1
2 3
7,8,9

4
5 6
"""