def solution(n):
    answer = []
    while n > 1:
        if n % 2 == 0:
            answer.append(n)
            n = n //2
        elif n % 2 == 1:
            answer.append(n)
            n = 3*n+1
    answer.append(n)
    return answer