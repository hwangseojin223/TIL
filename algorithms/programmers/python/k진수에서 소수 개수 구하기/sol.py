
def solution(n, k):
    word = ""
    while n>0 :            
        word = str(n%k) + word
        n = n//k
        
    word = word.split("0")  

    count = 0
    for w in word:
        if len(w) == 0:   # ''인 경우 패스
            continue
        if int(w) <= 1: # 1인 경우 패스
            continue
        is_prime = True
        for i in range(2, int(int(w)**0.5) +1): # 소수찾기
            if int(w)%i == 0:
                is_prime = False
                break
        if is_prime:
             count += 1
            
    return count