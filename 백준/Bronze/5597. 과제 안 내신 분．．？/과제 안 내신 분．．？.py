a = set(range(1, 31))
for i in range(28):
    b= int(input())
    a.discard(b)

c = list(a)
print(min(c))
print(max(c))