from itertools import product # 중복순열

def solution(word):
    dic = set()
    for k in product(['A','E','I','O','U',''], repeat=5):
        #''넣는이유 : A같은경우때문에
        dic.add("".join(k))
    dic = sorted(dic)
    for i, w in enumerate(dic):
        if w == word:
            return i