import sys
sys.stdin = open("input.txt", "r")

N, M, x, y, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))

# 우 좌 상 하
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 0번 인덱스 바닥, 5번 인덱스 위
#   1
# 3 0 2
#   4
#   5
dice = [0] * 6

for i in range(K):
    d = order[i] - 1
    nx = x + dx[d]
    ny = y + dy[d]

    if 0 <= nx < M and 0 <= ny < N:
        if d == 0:
            dice[2], dice[0], dice[3], dice[5] = dice[0], dice[3], dice[5], dice[2]
        elif d == 1:
            dice[3], dice[5], dice[2], dice[0] = dice[0], dice[3], dice[5], dice[2]
        elif d == 2:
            dice[1], dice[5], dice[4], dice[0] = dice[0], dice[1], dice[5], dice[4]
        elif d == 4:
            dice[4], dice[5], dice[1], dice[0] = dice[0], dice[4], dice[5], dice[1]

        if matrix[ny][nx] == 0:
            matrix[ny][nx] = dice[0]
        else:
            dice[0] = matrix[ny][nx]
            matrix[ny][nx] = 0

        print(dice[5])
        x, y = nx, ny