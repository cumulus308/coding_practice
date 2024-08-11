# 숫자의 개수 2577번
A = int(input())
B = int(input())
C = int(input())
count_list = [0]*10
result = str(A*B*C)
for i in range(10):
    print(result.count(str(i)))