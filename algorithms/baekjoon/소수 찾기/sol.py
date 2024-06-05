import math
n = int(input())

cnt = 0
num = list(map(int, input().split()))

for i in num:
    if i == 1:
        continue
    for j in range(2, int(math.sqrt(i))+1):
        if i%j==0:
            break
    else:
        cnt += 1
print(cnt)