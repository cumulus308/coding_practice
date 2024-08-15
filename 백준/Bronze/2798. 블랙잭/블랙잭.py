# 블랙잭 # 2798번
N, M = map(int,input().split())
card = list(map(int,input().split()))

max_sum = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range (j+1, N):
            current_sum = card[i] + card[j] + card[k]
            if current_sum <= M and current_sum > max_sum:
                max_sum = current_sum
                
print(max_sum)