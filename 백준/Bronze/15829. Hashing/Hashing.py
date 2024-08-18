# Hashing # 15829번
L = int(input())
string = input()
r = 31
m = 1234567891
answer = 0
for i in range(L):
    answer += ((ord(string[i])-ord('a')+1) * (r**i) )
print(answer%m)