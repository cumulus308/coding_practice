import sys

N = int(input())
people = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

ranks = [1] * N
for i in range(N):
    for j in range(N):
        if i != j:
            if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
                ranks[i] += 1

print(' '.join(map(str, ranks)))