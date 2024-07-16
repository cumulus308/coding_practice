def solution(arr):
    
    for i in range(0,11):
        if len(arr) == 2**i:
            return arr
        
        elif len(arr)<2**i:
            num = 2**i - len(arr)
            temp = [0] * num
            return arr+temp