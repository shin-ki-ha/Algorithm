import sys
sys.stdin = open("input.txt", "r")

"""
마지막 날부터 첫째 날 순서로 DP 적용
"""

N = int(input())
arr = []
for _ in range(N):
    work = list(map(int, input().split()))
    arr.append(work)

dp = [0] * (N + 1)

for i in range(N-1, -1, -1):
    T, P = arr[i][0], arr[i][1]
    if i + T < N + 1:
        # 일 할 수 있는 날과 전날의 값을 비교하여 큰 값을 메모이제이션
        dp[i] = max(P + dp[i + T], dp[i + 1])
    else:
        dp[i] = dp[i + 1]
print(dp[0])