a,b = map(int,input().split())
c = input().split()
# d = ''
for i in c:
    if int(i) < b:
        print(i,end=" ")
