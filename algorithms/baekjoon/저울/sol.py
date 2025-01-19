n = int(input())
m = int(input())
inf = 987_654_321 # 무한대값을 표현 # ==987654321 #초기값은 inf로 설정하여 비교 결과가 없는 상태

graph = [[inf]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 플로이드-워셜 알고리즘으로 간접 경로 반영
for mid in range(1, n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            # 예시) inf > 1+1 인 경우
            if graph[start][end] > graph[start][mid] + graph[mid][end]:
                graph[start][end] = graph[start][mid] + graph[mid][end]

for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if graph[i][j] == inf and graph[j][i] == inf:
            count += 1
    print(count -1) # 자기자신 하나 빼기


# 다익스트라 알고리즘
# 플로이드-워셜 알고리즘