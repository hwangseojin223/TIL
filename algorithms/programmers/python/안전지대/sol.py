def solution(board):
    n = len(board) 
    danger = []
    for i in range(0, n): 
        for j in range(0, n): 
            if board[i][j] == 1:
                bomb = [[i-1, j-1], [i-1,j],[i-1, j+1],
                           [i,j-1],[i,j],[i,j+1],
                           [i+1, j-1],[i+1, j],[i+1, j+1]]
                for k in range(len(bomb)):
                    if bomb[k] not in danger:
                        danger +=  [bomb[k]]

    safe = []
    for m in range(len(danger)):
        if danger[m][0] >=0 and danger[m][1] >=0 and danger[m][0]<n and danger[m][1]<n:
            safe += [danger[m]]
    all = n*n
    if all == len(safe):
        return 0
    else:
        zero = all - len(safe)          
        return zero