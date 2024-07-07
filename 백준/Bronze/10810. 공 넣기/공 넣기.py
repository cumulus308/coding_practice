a,b = map(int,input().split())
list = [0 for x in range(a)]
for _ in range(b):
    i, j, k = map(int,input().split())
    for __ in range(i-1,j):
        list[__] = k

for q in range(a):
    print(list[q],end=" ")