def solution(emergency):
    a = list(enumerate(emergency,start=1))
    b =sorted(a,key= lambda x : x[1],reverse = True)
    answer = []
    for i in a:
        answer.append(b.index(i)+1)
    
    
    return answer