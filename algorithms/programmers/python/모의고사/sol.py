def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    s1, s2, s3 = 0, 0, 0
    
    for idx, num in enumerate(answers):
        if num == one[idx%5]:
            s1 += 1
        if num == two[idx%8]:
            s2 += 1
        if num == three[idx%10]:
            s3 += 1
    score = [s1, s2, s3]
    result = []
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)
    return result