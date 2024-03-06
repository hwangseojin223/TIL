def solution(array, commands):
    answer = []
    for i in commands:
        a = i[0]-1
        b = i[1]-1
        tmp = array[a:b+1]
        tmp.sort()
        c = i[2]-1
        num = tmp[c]
        answer.append(num)
    return answer

# 다른사람 풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))