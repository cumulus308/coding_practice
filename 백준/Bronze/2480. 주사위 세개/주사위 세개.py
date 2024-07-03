a,b,c = input().split()

if a==b and b==c:
    print(10000+int(a)*1000)
elif a == b:
    print(1_000+int(a)*100)
elif c == b:
    print(1_000+int(b)*100)
elif a == c:
    print(1_000+int(a)*100)
else:
    print(int(max(a,b,c))*100)