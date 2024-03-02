# 최대공배수 
def gcd(a, b):
    for i in range(min(a,b), 0, -1):
        if a%i == 0 and b%i==0 :
            return i
        
def solution(numer1, denom1, numer2, denom2):
    # denom1, denom2 서로소 관계가 아닌 경우
    if denom2 % denom1 == 0 : 
        numer1 = numer1 * (denom2//denom1)
        denom1 = denom1 * (denom2//denom1)
    
    # denom1, denom2 서로소 관계인 경우
    else:
        numer1 *= denom2
        numer2 *= denom1
        denom2 *= denom1
    
    # 분수 덧셈
    numer3 = numer1 + numer2
    denom3 = denom2
    
    # 기약 분수 만들기
    tmp = gcd(numer3, denom3)
    numer3 = numer3 // tmp
    denom3 = denom3 // tmp 
    answer = [numer3, denom3]
    return answer