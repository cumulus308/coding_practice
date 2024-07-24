def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer and len(answer) < k:
            answer.append(i)
            if len(answer) == k:
                return answer
    if len(answer) < k:
        num = k - len(answer)
        answer += [-1] * num
        
    return answer