def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in arr:
        if len(answer) >0 and i != answer[-1]:
            answer.append(i)
            
    return answer

# 다른 사람 풀이
def no_continuous(s):
    # 함수를 완성하세요
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a