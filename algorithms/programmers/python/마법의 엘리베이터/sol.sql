# 23/100

def solution(storey):
    answer = 0
    while storey > 0:
        storey, na = divmod(storey, 10)

        if na > 5 or (storey%10 >= 5 and na == 5): # 5보다큰경우는10으로
            answer = answer + (10 - na)
            storey = storey + 1

        else: #elif na < 5 or (mok%10 < 5 and na == 5): # 5보다 작은경우는 하나씩 카운트
            answer = answer +  na
            # storey = storey - 1
            a = storey%10
            storey = storey - a#(storey%10)
            answer = answer + a#(storey%10)

    return answer