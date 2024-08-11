test_num = int(input())
for i in range(test_num):
    answer = ''
    num, string = input().split()
    for j in string:
        answer += j*int(num)
    print(answer)
    