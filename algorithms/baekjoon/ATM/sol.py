n = int(input())
time = list(map(int, input().split()))

time = sorted(time) 
result = 0

for i in range(len(time)):
    tmp = 0
    for j in range(i+1):
        tmp += time[j]
    result += tmp
    
print(result)