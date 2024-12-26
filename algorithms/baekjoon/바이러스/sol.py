computer_cnt = int(input())
link = int(input())
matrix = [[0]*(computer_cnt+1) for _ in range(computer_cnt+1)]

for _ in range(link):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
    
visited_computer = [0] * (computer_cnt + 1)

def visited(v):
    visited_computer[v] = 1
    for i in range(1, computer_cnt + 1):
        if matrix[v][i] == 1 and visited_computer[i] == 0:
            visited(i)
            
visited(1)
print(sum(visited_computer)-1)
