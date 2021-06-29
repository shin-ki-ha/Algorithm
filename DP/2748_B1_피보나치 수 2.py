# 메모이제이션을 활용한 피보나치 수 구현
n = int(input())
fibo = [0, 1]

if n > 1:
    for i in range(2, n+1):
        result = fibo[i - 1] + fibo[i - 2]
        fibo.append(result)

print(fibo[n])
