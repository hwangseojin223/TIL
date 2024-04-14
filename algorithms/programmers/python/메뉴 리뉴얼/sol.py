from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        tmp = []
        for order in orders:
            for li in combinations(order, c):
                res = ''.join(sorted(li))
                tmp.append(res)
        sorted_tmp = Counter(tmp).most_common()
        for menu, cnt in sorted_tmp:
            if cnt > 1 and cnt == sorted_tmp[0][1]:
                answer.append(menu)
    return sorted(answer)

"""
# combination : 조합 #

import itertools

arr = ['A', 'B', 'C']
nCr = itertools.combinations(arr, 2)
print(list(nCr))

결과 : [('A', 'B'), ('A', 'C'), ('B', 'C')]

------------------------------------------

# Counter #
from collections import Couter
>>> Counter(["hi", "hey", "hi", "hi", "hello", "hey"])
Counter({'hi': 3, 'hey': 2, 'hello': 1})

>>> Counter("hello world")
Counter({'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

"""

