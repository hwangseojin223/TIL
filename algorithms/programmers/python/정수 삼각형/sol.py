def solution(triangle):
    height = len(triangle)
    
    dp = [[0] * i for i in range(1, height+1)]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, height):
        for j in range(0, i+1):
            if j==0 : # 맨 왼쪽 열
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i: # 맨 오른쪽 열
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else: 
                dp[i][j] =  max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    return max(dp[-1])