# N, M = map(int, input().split())

# basket = [b for b in range(1, N + 1)]

# for _ in range(M):
#     i, j = map(int, input().split())
#     basket = list(reversed(basket[i-1:j+1]))

# for b in range(N):
#     print(b, end=' ')

N, M = map(int, input().split())

basket = [b for b in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    basket[i-1:j] = reversed(basket[i-1:j])  # 특정 범위만 역순으로 뒤집기

print(*basket)