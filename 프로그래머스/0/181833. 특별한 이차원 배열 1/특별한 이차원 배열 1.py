def solution(n):
    answer = []
    for i in range(n):
            answer.append([0 for x in range(n)])
    for j in range(n):
        answer[j][j] = 1
    return answer