def solution(s):
    answer = ''
    return s[len(s)//2] if len(s)% 2==1 else s[int(len(s)//2-1):int(len(s)//2) + 1]