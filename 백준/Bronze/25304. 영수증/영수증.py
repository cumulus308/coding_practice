a = int(input())
b= int(input())
c= 0
for _ in range(b):
    d,f = input().split()
    c += int(d)*int(f)

print( "Yes") if a == c else print( "No")