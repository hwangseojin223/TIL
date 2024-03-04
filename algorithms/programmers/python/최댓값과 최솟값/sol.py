def solution(s):
    lst = []
    for i in s.split(' '):
        lst.append(int(i))
    return f'{min(lst)} {max(lst)}'