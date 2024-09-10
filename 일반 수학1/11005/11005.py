def solution(N, B):
    # 변환에 필요한 문자들
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    result = ""
    
    # N을 B로 나누며 나머지를 result에 쌓기
    # N이 0이 될 때까지 과정 반복
    while N > 0:
        N, remainder = divmod(N, B)
        result = digits[remainder] + result
    
    return result


N, B = map(int, input().split())
print(solution(N, B))