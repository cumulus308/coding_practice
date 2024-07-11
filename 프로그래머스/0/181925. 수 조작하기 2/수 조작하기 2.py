def solution(numLog):
    new_numLog = numLog[1:]
    result = ''
    for i in range(len(new_numLog)):
        dis = new_numLog[i] - numLog[i]
        if dis == 1:
            result += "w"
        elif dis == -1:
            result += "s"
        elif dis == 10:
            result += "d"
        elif dis == -10:
            result += "a"            
    return result