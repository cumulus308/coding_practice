def solution(food):
    result = []
    
    for i in range(1, len(food)):
        result.extend([str(i)] * (food[i] // 2))
    
    left = ''.join(result)
    right = left[::-1]
    
    return left + '0' + right