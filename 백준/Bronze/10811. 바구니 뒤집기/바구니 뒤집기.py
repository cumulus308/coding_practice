a,b = map(int,input().split())

list_a = [x for x in range(1,a+1)]
for _ in range(b):
    i,j = map(int,input().split())
    list_a[i-1:j] = reversed(list_a[i-1:j])
print(*list_a)

