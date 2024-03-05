def solution(s):
    answer = True
    A = []
    for i in s:
        if i == '(':
            A.append(i)
        else: # ')'인 경우
            if len(A) >0 and A[-1] == '(':
                A.pop()
            else:
                A.append(i)
    if len(A) == 0:
        return True
    else:
        return False
        