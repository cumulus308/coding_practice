def solution(s):
    answer = []
    for i in range(len(s)):
        if s[:i][::-1].find(s[i]) == -1:
            answer.append(s[:i][::-1].find(s[i]))
        else:
            answer.append(s[:i][::-1].find(s[i])+1)
    return answer