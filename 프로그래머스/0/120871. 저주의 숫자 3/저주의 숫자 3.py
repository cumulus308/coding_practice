# def solution(n):
#     a = [x for x in range(200) if x % 3 != 0 and '3' not in str(x)]

#     return a[n-1]

def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer