def solution(balls, share):
    n = 1
    m = 1
    b = 1
    for i in range(1,balls +1):
        n *= i
    for j in range(1,share +1):
        m *= j
    for k in range(1,(balls - share +1)):
        b *= k  
        
    
    

    return n / (m * b)