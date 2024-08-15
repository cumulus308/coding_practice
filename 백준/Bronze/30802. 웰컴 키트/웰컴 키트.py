# 웰컴 키트 # 30802번
N = int(input())
size_count = list(map(int,input().split()))
T, P = map(int, input().split())

result1 = sum([(size_num-1) // T + 1 for size_num in size_count])
num1, num2 = divmod(N,P)

print(result1)
print(num1, num2)