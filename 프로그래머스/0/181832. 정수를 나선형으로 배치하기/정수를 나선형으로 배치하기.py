def solution(n):
    answer = [[0] * n for _ in range(n)]
    
    x, y = 0, 0
    dir = 0 # 0(→), 1(↓), 2(←), 3(↑)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    for i in range(1, n**2+1):
        answer[x][y] = i
        
        nx = x + dx[dir]
        ny = y + dy[dir]
        
        # 벽에 닿거나, 다음 칸에 0이 아닌 것이 들어가 있는 경우
        if not(0 <= nx < n and 0 <= ny < n) or answer[nx][ny] != 0:
            dir = (dir + 1) % 4	# 방향 전환
            nx = x + dx[dir]
            ny = y + dy[dir]
        
        x, y = nx, ny        
        
    return answer