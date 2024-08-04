def solution(t, p):
    answer = 0
    return sum(1 for x in range(0,len(t)-len(p)+1) if int(t[x:x+len(p)]) <= int(p)  )