def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i]:
            sum_ = a + d*i
            answer += sum_
    return answer