def solution(d, budget):
    answer = 0
    sum_d = 0
    for i in sorted(d):
        if sum_d + i <= budget:
            sum_d += i
            answer += 1
        else:
            break
    return answer