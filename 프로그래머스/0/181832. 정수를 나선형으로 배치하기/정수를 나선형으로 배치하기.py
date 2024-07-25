def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    dx = [0, 1, 0, -1]  # 오른쪽, 아래, 왼쪽, 위
    dy = [1, 0, -1, 0]  # 오른쪽, 아래, 왼쪽, 위
    x, y = 0, 0
    direction = 0

    for i in range(1, n*n + 1):
        answer[x][y] = i
        
        nx, ny = x + dx[direction], y + dy[direction]

        if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny] != 0:
            direction = (direction + 1) % 4
            nx, ny = x + dx[direction], y + dy[direction]

        x, y = nx, ny
    
    return answer