import sys
input =sys.stdin.readline

a= int(input().rstrip())
for _ in range(a):
    b,c= map(int,input().split())
    print(b+c)