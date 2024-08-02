# 최대 공약수
def gcd(a,b):
    return b if a % b == 0 else gcd(b, a%b)

# 최소 공배수
def lcm(a,b):
    return (a*b) // gcd(a,b)

def solution(a,b):
    return [gcd(a,b), lcm(a,b)]