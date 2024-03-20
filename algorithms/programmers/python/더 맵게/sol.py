# heap

import heapq

def solution(scoville, K):

    heapq.heapify(scoville) 
    cnt = 0
    while(len(scoville)>=2 and scoville[0] < K):
        fir = heapq.heappop(scoville)
        sec = heapq.heappop(scoville)
        mix = fir + sec*2
        heapq.heappush(scoville, mix)
        cnt +=1
    if len(scoville)==1 and scoville[0]<K:
        return -1

    return cnt