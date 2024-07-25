def solution(picture, k):
    answer = []
    temp1 = ""
    
    for i in picture:
        for j in i:
            temp1 += j*k
        for _ in range(k):
            answer.append(temp1)
        temp1 = ""
    return answer