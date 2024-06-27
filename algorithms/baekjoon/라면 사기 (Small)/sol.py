# https://velog.io/@qazws78941/python%EB%B0%B1%EC%A4%80-17420-%ED%92%80%EC%9D%B4 
import math

n = int(input())

rest = list(map(int, input().split()))
plan = list(map(int, input().split()))

arr = []
for r, p in zip(rest, plan):
    arr.append([r,p])
    
arr = sorted(arr, key=lambda x : (x[1], x[0]))
# 계획일을 기준으로 정렬, 계획이 같으면 남은기간 순으로 정렬

p = arr[0][0]
th = arr[0][0]
cnt = 0
for i in range(n):
    if th > arr[i][0] : # 남은 기간이 기준점보다 짧다면 연장
        tmp = math.ceil((th-arr[i][0])/30)
        cnt += tmp
        arr[i][0] += tmp * 30
    p = max(p, arr[i][0])
		
    # 다음 계획일의 구간의 값이 달라진다면 구간 기준점 재정의
    if i+1 < n and arr[i][1] != arr[i+1][1]:
        th = max(p, arr[i+1][1])
print(cnt)