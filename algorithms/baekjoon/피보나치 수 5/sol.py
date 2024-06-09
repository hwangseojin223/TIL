def fi(n):
    answer = 0
    if n == 0:
        answer = 0
    elif n == 1:
        answer = 1
    else:
        answer = fi(n-1)+fi(n-2)
    return answer

n = int(input())
answer = fi(n)
print(answer)