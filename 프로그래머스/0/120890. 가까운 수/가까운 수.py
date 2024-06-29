def solution(array, n):
    b = sorted(array)[::-1]
    minus = float('inf')
    answer = []
    for i in b:
        if minus >= abs(n-i):
            minus = abs(n-i)
            answer = i
        
    return answer