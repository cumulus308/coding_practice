number = list(input().split(" "))
answer = sum(int(x)**2 for x in number) % 10
print(answer)