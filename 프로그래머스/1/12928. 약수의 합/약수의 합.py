# def solution(n):
#     answer = []
#     for i in range(1,int(n**0.5)+1):
#         if n % i == 0:
#             answer.append(i)
#             if i != n//i:
#                 answer.append(n//i)
#     return sum(answer)
def solution(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])