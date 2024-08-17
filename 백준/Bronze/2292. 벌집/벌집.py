# 벌집 # 2292번
N = int(input())

n = 1
while True:
    if 3*n**2 - 3*n + 1 >= N:
        print(n)
        break
    n += 1