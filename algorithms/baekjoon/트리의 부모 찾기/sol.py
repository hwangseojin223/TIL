node_cnt = int(input())
matrix = [[] for _ in range(node_cnt+1)]

for i in range(node_cnt-1):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

# 부모를 담을 변수
visited = [0] * (node_cnt+1)

def dfs(v):
    for i in matrix[v]:
        if not visited[i]:
            visited[i]=v
            dfs(i)
        
dfs(1)

for i in range(2, node_cnt+1):
    print(visited[i])