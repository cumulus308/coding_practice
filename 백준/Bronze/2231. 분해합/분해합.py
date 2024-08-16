def find(num):
    for i in range(1, num):
        if i + sum(int(j) for j in str(i)) == num:
            return i
    return 0

num = int(input())
print(find(num))