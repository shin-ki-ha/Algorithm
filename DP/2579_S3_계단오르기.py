import sys
sys.stdin = open("input.txt", "r")

"""
연속해서 3개의 계단을 밟을 수 없는 조건의 점화식 도출
1. 두 칸 전의 계단은 밟아도 상관 없음
2. 한 칸 전의 계단을 밟은 경우 두 칸 전의 계단을 밟으면 안되기 때문에 한 칸 전의 계단의 두 칸 전 계단의 값을 DP에 더해줌
둘 중 큰 숫자가 DP
"""

N = int(input())

stair = [0]
for _ in range(N):
    stair.append(int(input()))

if N == 1:
    print(stair[1])
else:
    dp = [0] * (N+1)
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]

    for i in range(3, N+1):
        dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])

    print(dp[N])