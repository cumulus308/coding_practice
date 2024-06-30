def solution(array):
    a = {}
    for i in array:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
            
    b= sorted(a.items(), key= lambda x : x[1])
    
    if len(b) >1 and b[-1][1] == b[-2][1]:
        return -1
    else:
        return b[-1][0]