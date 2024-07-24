def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        a = [arr[x] for x in range(s,e+1) if arr[x]>k]
        if a:
            answer.append(min(a))
        else:
            answer.append(-1)
    return answer 