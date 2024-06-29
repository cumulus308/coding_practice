def solution(n):
    a = []
    for i in range(n+1):
        if i % 2 == 0:
            a.append(i)
    answer = sum(a)
    return answer