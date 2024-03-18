# hash

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i,j in zip(participant, completion):
        if i != j:
            return i

    return participant[-1]


# 다른 풀이
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]