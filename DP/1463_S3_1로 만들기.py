X = int(input())
memo = [0] * (X + 1)

"""
최소 연산 횟수 = 해당 숫자의 2 또는 3으로 나눈 몫의 값에 +1을 더한 것

더 나은 해결 방법 : 기본값은 전 값의 +1로 둔 뒤 나누어 떨어질 경우 작은 수를 메모이제이션하면 된다
"""

for i in range(2, len(memo)):
    # 2와 3 둘 다 나누어 떨어질 경우
    if i % 2 == 0 and i % 3 == 0:
        a = memo[i // 2] + 1
        b = memo[i // 3] + 1
        if a > b:
            memo[i] = b
        else:
            memo[i] = a

    # 2로만 나누어 떨어지는 경우
    elif i % 2 == 0:
        memo[i] = memo[i//2] + 1

    # 3으로만 나누어 떨어지는 경우
    elif i % 3 == 0:
        memo[i] = memo[i//3] + 1

    # 현재 메모이제이션 값이 전 값의 +1보다 큰 경우 바꾸기
    if memo[i - 1] + 1 < memo[i]:
        memo[i] = memo[i - 1] + 1
    # 현재 메모이제이션 값이 0인 경우, 나누어떨어지지 않으므로 전 값에 +1을 최소값으로 지정
    elif memo[i] == 0:
        memo[i] = memo[i - 1] + 1

print(memo[X])