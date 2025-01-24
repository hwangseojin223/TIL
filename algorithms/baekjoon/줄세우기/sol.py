n = int(input())
dp = [1] * (n+1) # LIS를 저장할 DP 테이블, 초기값은 모두 1

line = [0]
for _ in range(n):
    line.append(int(input()))
    

# LIS(가장 긴 증가하는 부분 수열) 계산
for i in range(1, n+1): # 현재 고려 중인 번호
    for j in range(1, i): # i보다 앞에 있는 번호
        if line[j]< line[i]: # (앞 번호가 더 작을 때만 증가 가능)
            dp[i] = max(dp[i], dp[j]+1) ## LIS 길이 갱신

# 최소 이동 횟수 계산 
# n-LIS의 길이 출력
# LIS의 길이를 max(d)로 구합니다.
# 최소 이동 횟수는 전체 아이들 수 - LIS 길이
print(n-max(dp))