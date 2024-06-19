n = int(input())
n_list=[]
for i in range(n):
    weight, height = map(int, input().split())
    n_list.append([weight, height])

grade = []

for i in range(0,len(n_list)):
    tmp = 1
    for j in range(0, len(n_list)):
        if n_list[i][0] < n_list[j][0] and n_list[i][1] < n_list[j][1]:
            tmp += 1
    grade.append(tmp)
    
print(*grade)