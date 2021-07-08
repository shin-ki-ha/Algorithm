import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    M, N = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    B = [0] + list(map(int, input().split()))
    charge = [] # 충전기를 담을 리스트
    total = 0 # 결과

    # 충전기를 담은 뒤 파워 순서로 정렬
    for _ in range(N):
        x, y, c, p = map(int, input().split())
        charge.append([x-1, y-1, c, p])

    charge.sort(key= lambda x : x[3], reverse=True)

    # 노, 상, 우, 하, 좌
    nx = [0, 0, 1, 0, -1]
    ny = [0, -1, 0, 1, 0]

    # 사용자 시작 인덱스
    A_x, A_y = 0, 0
    B_x, B_y = 9, 9

    for i in range(M + 1):
        total_A = [] # A 사용자가 사용할 수 있는 충전소의 파워를 담을 리스트
        total_B = [] # B 사용자가 사용할 수 있는 충전소의 파워를 담을 리스트

        # 사용자 위치 이동
        A_x += nx[A[i]]
        A_y += ny[A[i]]
        B_x += nx[B[i]]
        B_y += ny[B[i]]
        for j in range(N):
            charge_x = charge[j][0]
            charge_y = charge[j][1]
            charge_size = charge[j][2]
            charge_power = charge[j][3]

            # 충전할 수 있는 거리인지 확인
            D_A = abs(A_x - charge_x) + abs(A_y - charge_y)
            D_B = abs(B_x - charge_x) + abs(B_y - charge_y)

            # 충전소가 2개 이상 필요없기 때문에 제한
            if len(total_A) < 2:
                if D_A <= charge_size:
                    total_A.append((j, charge_power))
            if len(total_B) < 2:
                if D_B <= charge_size:
                    total_B.append((j, charge_power))

        # 충전 조건
        # A만 충전할 수 있다면 A의 값만 더하기
        if len(total_A) != 0 and len(total_B) == 0:
            total += total_A[0][1]
        # B만 충전할 수 있다면 B의 값만 더하기
        elif len(total_A) == 0 and len(total_B) != 0:
            total += total_B[0][1]
        # 둘 다 충전할 수 있다면
        elif total_A and total_B:
            # A와 B의 값이 다르다면 둘 다 값 더하기
            if total_A[0] != total_B[0]:
                total += total_A[0][1]
                total += total_B[0][1]
            # 두 값이 같다면 하나만 더하기
            else:
                total += total_A[0][1]
                # 겹치는데 둘 다 하나만 가지고 있다면 반복문 넘기기
                if len(total_A) == 1 and len(total_B) == 1:
                    continue
                # A가 더 길다면 A의 뒤에 충전값 더하기
                elif len(total_A) > len(total_B):
                    total += total_A[1][1]
                # B가 더 길다면 B의 뒤에 충전값 더하기
                elif len(total_A) < len(total_B):
                    total += total_B[1][1]
                # 둘 다 2개의 충전값을 가지고 있다면 더 큰 값 더하기
                else:
                    total += max(total_A[1][1], total_B[1][1])
        else:
            continue

    print('#{} {}'.format(tc, total))





