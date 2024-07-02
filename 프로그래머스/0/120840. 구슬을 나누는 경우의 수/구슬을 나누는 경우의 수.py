def solution(balls, share):
    answer = mul(balls) / (mul(balls-share)*mul(share))
    return answer
    
def mul(m):
    result = 1
    for i in range(1,m +1):
        result *= i
    return result


# def solution(balls, share):
#     answer = factorial(balls) / (factorial(balls - share) * factorial(share))
#     return answer

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result = result * i
#     return result
#     n = 1
#     m = 1
#     b = 1
#     for i in range(1,balls +1):
#         n *= i
#     for j in range(1,share +1):
#         m *= j
#     for k in range(1,(balls - share +1)):
#         b *= k  
        
    
    

#     return n / (m * b)