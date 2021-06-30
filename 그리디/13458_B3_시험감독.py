import sys
sys.stdin = open("input.txt", "r")

"""
완전탐색
총감독관 감시 인원 뺀 뒤 나머지를 부감독관이 감시하도록 알고리즘 작성
"""

N = int(input())
room = list(map(int, input().split()))
m, s = map(int, input().split()) # m : 총감독관의 감시수, s : 부감독관의 감시수

total = 0 # 필요한 감독관의 수
for i in room:
    # 총감독관 할당량
    i -= m
    total += 1

    # 부감독관 할당량
    if i < 1:
        continue
    else:
        # 감시 인원이 나누어 떨어지지 않을 경우 필요한 감독관 수 + 1
        if i % s:
            a = ((i // s) + 1)
        # 감시 인원이 나누어 떨어질 경우 필요한 감독관 수
        else:
            a = (i // s)

        total += a

print(total)