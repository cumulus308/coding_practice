def solution(n):
    num = n - 1
    for i in range(2,int(n**0.5)+1):
        if num % i ==0:
            return i
    return num