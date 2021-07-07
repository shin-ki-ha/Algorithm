import sys
sys.stdin = open("input.txt", "r")

"""
냅색 알고리즘
"""

N, K = map(int, input().split())
thing = [[0, 0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    thing.append(list(map(int, input().split())))

for i in range(1, N + 1):
    for j in range(1, K + 1):
        w = thing[i][0]
        v = thing[i][1]

        if j < w:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(v + knapsack[i - 1][j - w], knapsack[i - 1][j])

print(knapsack)

