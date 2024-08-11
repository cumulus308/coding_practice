test_num = int(input())
for _ in range(test_num):
    score = 0
    result = []
    answer = input()
    for i in answer:
        if i == "O":
            score += 1
            result.extend([score])
        else:
            score = 0
            
    print(sum(result))