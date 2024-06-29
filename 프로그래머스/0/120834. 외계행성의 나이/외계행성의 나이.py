def solution(age):
    a =[]
    for j in str(age):
        for i in enumerate(range(ord('a'),ord('k'))):
        
            if str(i[0]) == j:
                a.append(chr(i[1]))
    return "".join(a)