# 다른 사람 코드
# **최대 heap**
import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    works = [-work for work in works]
    heapq.heapify(works)

    for _ in range(n):
        work = heapq.heappop(works) + 1
        heapq.heappush(works, work)

    result = sum([work**2 for work in works])
    return result

# 효율성 통과 x
# def solution(n, works):
#     for i in range(n):
#         works.sort()
#         max_work = works.pop()
#         if max_work == 0:
#             return 0
#         else:
#             max_work -= 1
#             works.append(max_work)
#     answer = 0
#     for j in range(len(works)):

#         answer += works[j]**2
#     return answer