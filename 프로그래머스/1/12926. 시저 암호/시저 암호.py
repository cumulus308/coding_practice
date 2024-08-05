def solution(s, n):
    answer = ''
    UPPER = ('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ')
    LOWER = UPPER.lower()
    for i in s:
        if i.isupper():
            answer += UPPER[UPPER.index(i)+n]
        elif i.islower():
            answer += LOWER[LOWER.index(i)+n]
        else:
            answer += i
    return answer