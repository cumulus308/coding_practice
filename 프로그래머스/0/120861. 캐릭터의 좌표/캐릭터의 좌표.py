def solution(keyinput, board):
    location = [0,0]
    move = {"left": (-1,0), "right": (1,0), "up": (0,1), "down": (0,-1)}
    for i in keyinput:
        if abs(location[0] + move[i][0]) < board[0]/2:
            location[0] = location[0]+ move[i][0]
        if abs(location[1] + move[i][1]) < board[1]/2:
            location[1] = location[1]+ move[i][1]
    return location