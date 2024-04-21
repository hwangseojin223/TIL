# 100점 아님

from collections import defaultdict

def solution(board):
    counts = defaultdict(int)
    
    for r in range(len(board)):
        for c in range(len(board[0])):
            grid = board[r][c]
            counts[grid] += 1
    
    ocnt = counts['O']
    xcnt = counts['X']
    # 시작안한 경우 => 1
    if counts['O'] == 0 and counts['X'] == 0:
        return 1
    # 둘의 개수가 2보다 작으면서 같은 경우 -> 1
    if counts['O'] == counts['X'] and counts['O'] <= 2:
        return 1
    # O의 개수 = X의 개수+1 이 아닌 경우 => 0
    if not (counts['O'] == counts["X"]+1):
        return 0
    
    
    owin = 0
    xwin = 0
    
    col = list(zip(*board))

    # 가로 세로
    for i in board:
        if board[i].count('O') == 3 or col[i].count('O')==3:
            owin += 1
        if board[i].count('X')== 3 or col[i].count('X')==3:
            xwin += 1

    
    # 대각선
    for i in range(0, 3, 2):
        if board[0][i] == board[1][1] == board[2][2-i] == 'O':
            owin += 1
        if board[0][i] == board[1][1] == board[2][2-i] == 'X':
            xwin += 1
    # x가 이기고 o가 졌는데 o가 하나 더 둔 경우 {"OO.", "XXX", "OO."}
    # ["XXX", "XOO", "OOO"]
    if (ocnt >= xcnt) and xwin == 1 and owin==0:
        return 0
    # 둘다 이긴경우
    elif owin == 1 and xwin == 1:
        return 0
    # o가 이기고 x가 진 경우, o가 지고 x가 진 경우 -> 1
    elif (owin ==1 and xwin==0) or (owin==0 and xwin==1 ):
        return 1
    