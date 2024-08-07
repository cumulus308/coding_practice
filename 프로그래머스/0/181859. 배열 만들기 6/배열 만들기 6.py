def solution(arr):
    answer = []
    for num in arr:
        if not answer or num != answer[-1]:
            answer.append(num)
        else:
            answer.pop()
    
    return answer if answer else [-1]