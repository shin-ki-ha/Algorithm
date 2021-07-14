import sys
sys.stdin = open("input.txt", "r")

def bfs(x, y):
    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    stack.append([x, y])
    visit[y][x] = 1
    while stack:
        x1, y1 = stack.pop()
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if matrix[ny][nx] == 1 and visit[ny][nx] == 0:
                    visit[ny][nx] = 1
                    stack.append([nx, ny])

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    matrix = [[0 for _ in range(M)] for _ in range(N)]
    visit = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0

    for _ in range(K):
        X, Y = map(int, input().split())
        matrix[Y][X] = 1

    for i in range(N):
        for j in range(M):
            stack = []
            if matrix[i][j] == 1 and visit[i][j] == 0:
                cnt += 1
                bfs(j, i)

    print(cnt)