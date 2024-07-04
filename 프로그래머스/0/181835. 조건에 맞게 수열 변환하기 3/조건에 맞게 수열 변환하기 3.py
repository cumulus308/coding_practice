def solution(arr, k):
    answer = []
    if k % 2 ==1:
        for i in arr:
            answer.append(k*i)
    elif k % 2 ==0:
        for j in arr:
            answer.append(k+j)

    return answer