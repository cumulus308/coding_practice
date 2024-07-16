def solution(myString, pat):
    answer = 0
    a= len(pat)
    for i in range(len(myString)):
        if myString[i:i+a] == pat:
            answer += 1
    return answer