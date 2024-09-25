N, M = map(int, input().split())

basket = [x for x in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

for i in range(N):
    print(basket[i], end=' ')