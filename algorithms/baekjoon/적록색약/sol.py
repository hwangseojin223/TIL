from collections import deque

n = int(input())
line = [list(input()) for _ in range(n)]
q = deque()


def bfs(x, y):
    q.append((x,y))
    dx = [-1, 0, 1, 0] # 상, 우, 하, 좌
    dy = [0, 1, 0, -1]
    visited[x][y] = 1 # 현재 위치 방문 처리
    while q:
        x, y = q.popleft() # 큐에서 가장 앞에 있는 위치 꺼냄
        for d in range(4): # 상하좌우 탐색
            nx = x + dx[d]
            ny = y + dy[d]
            # 조건: 인덱스 유효 범위 내, 같은 색이어야하고 , 방문하지 않았어야 함
            if 0<=nx<n and 0<=ny<n and line[nx][ny]==line[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1 # 방문 처리
                q.append((nx, ny)) # 큐에 추가
    
    
# 적록색약 아닌 경우
visited = [[0] * n for _ in range(n)]
cnt1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt1 += 1 # 구역 하나 완료
            
            
# 적록색약
for i in range(n):
    for j in range(n):
        if line[i][j] == 'G':
            line[i][j] = 'R'
visited = [[0] * n for _ in range(n)]
cnt2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt2 += 1
            
print(cnt1, cnt2)