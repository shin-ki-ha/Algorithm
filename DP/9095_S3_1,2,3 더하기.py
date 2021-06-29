import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    memo = [0, 1, 2, 4]

    if n > 3:
        for i in range(4, n + 1):
            # 점화식
            result = memo[i - 1] + memo[i - 2] + memo[i - 3]
            memo.append(result)
    print(memo[n])