# Hashing # 15829번
L = int(input())
strings = input()
answer = 0
for i, string in enumerate(strings):
    answer += (ord(string)-ord('a')+1) * (31**i)
print(answer)