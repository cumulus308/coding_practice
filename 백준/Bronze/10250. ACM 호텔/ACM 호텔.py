test = int(input())
for _ in range(test):
    H, W, N = map(int,input().split())
    floor = (N-1) % H +1
    room = (N-1) // H +1
    print(f'{floor}{room:02d}')