def solution(n):
    count1 = 0
    for i in range(n+1):
        count2 = 0
        for j in range(1,i+1):
            if i % j ==0:
                count2 += 1
        if count2 >=3:
            count1 += 1
    
    
    return count1
