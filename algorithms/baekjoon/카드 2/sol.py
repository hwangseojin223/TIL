from collections import deque

n = int(input())
cards = [i+1 for i in range(n)]

cards = deque(cards)
while len(cards)>1:
    cards.popleft()
    cards.rotate(-1)
print(*cards)