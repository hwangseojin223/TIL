N = int(input())
color_map = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0

def cut(row, col, n):
    global white, blue
    
    color = color_map[row][col]
    
    for i in range(row, row+n):
        for j in range(col, col+n):
            if color != color_map[i][j]:
                next = n // 2
                cut(row, col, next)
                cut(row, col+next, next)
                cut(row+next, col, next)
                cut(row+next, col+next, next)
                return
    if color == 0:
        white += 1
    else:
        blue += 1
    return 

cut(0, 0, N)
print(white)
print(blue)