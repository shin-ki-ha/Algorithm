import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    nums = list(input())
    L = N // 4
    result = set()

    for _ in range(L):
        for i in range(4): # 4면
            # 1면에 들어가는 숫자
            result.add(''.join(nums[i*L:(i+1)*L]))
        nums.append(nums.pop(0))

    result_list = []
    for i in result:
        # 16진수를 10진수로 변환
        result_list.append(int(i, 16))

    result_list.sort(reverse=True)
    print('#{} {}'.format(tc, result_list[K-1]))