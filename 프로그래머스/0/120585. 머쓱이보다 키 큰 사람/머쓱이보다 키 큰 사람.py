def solution(array, height):
    ss = 0
    for i in array:
        if i > height:
            ss += 1
    answer = ss
    return answer

