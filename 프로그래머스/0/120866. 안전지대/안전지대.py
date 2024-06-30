def solution(board):
    n = len(board)
    safe = n*n
    mines =[]
    
    #지뢰위치표시
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                mines.append((i,j))
                safe -= 1
    
    #주변 지뢰 표시
    for x,y in mines: 
        for a in [-1,0,1]:
            for b in [-1,0,1]:
                nx,ny = x+a,y+b
                if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0:
                    board[nx][ny] =2
                    safe -= 1
    
    return safe
    
    
    