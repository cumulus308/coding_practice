def solution(num_list):
    mul = 1
    for i in num_list:
        mul *= i
    mul_1 = sum(num_list)**2
    
    return int(mul<mul_1)