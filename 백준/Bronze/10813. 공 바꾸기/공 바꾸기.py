a,b = map(int,input().split())
list = [x for x in range(1,1+a)]
for i in range(b):
    j, k = map(int,input().split())
    list[j-1],list[k-1] = list[k-1],list[j-1]
        

for q in range(a):
    print(list[q],end=" ")