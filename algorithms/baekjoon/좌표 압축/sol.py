"""
n = int(input())
num_list = list(map(int, input().split())) 

sort_list = sorted(set(num_list))
result = []

for i in num_list:
    tmp = sort_list.index(i)
    result.append(tmp)

print(*result)
"""

n = int(input())
num_list = list(map(int, input().split()))

sort_list = sorted(set(num_list))

dict_list = {}
for index, value in enumerate(sort_list):
    dict_list[value] = index

result = []
for num in num_list:
    result.append(dict_list[num])
    
print(*result)