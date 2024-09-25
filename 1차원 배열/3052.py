# result = []

# for _ in range(10):
#     n = int(input())
#     result.append(n)

# answer = []
# for i in result:
#     answer.append(i % 42)

# answer = set(answer)

# count = 0
# for _ in answer:
#     count += 1
# print(count)

# 짧은 풀이
arr = []

for i in range(10):
    a = int(input())
    if a % 42 not in arr:
        arr.append(a % 42)
print(len(arr))