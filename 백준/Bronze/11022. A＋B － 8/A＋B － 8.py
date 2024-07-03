t = int(input())
a_list = []

for i in range(t):
    j = input().split()
    a_list.append((j))

count = 1
for l in a_list:
    print(f'Case #{count}: {l[0]} + {l[1]} = {int(l[0]) + int(l[1])}')
    count += 1
