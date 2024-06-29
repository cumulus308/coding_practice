def solution(num, k):
    a= 0
    b= list(str(num))
    for i in b:
        a+=1
        if str(k) not in b:
            return -1
        
        elif str(k) == i:
            return a
            break