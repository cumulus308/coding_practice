def solution(n):
    answer = n*6 / gcd(6,n)/6
    return int(answer)
    
    
def gcd(a,b):
    while b>0:
        a,b  = b, a%b
    return a
    
