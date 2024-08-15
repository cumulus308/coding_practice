# 최대공약수와 최소공배수
a, b = map(int,input().split())

# 최대 공약수
def gcd(a,b):
    return b if a % b == 0 else gcd(b, a%b)

# 최소 공배수
def lcm(a,b):
    return (a*b) // gcd(a,b)

print(gcd(a,b))
print(lcm(a,b))