def solution(my_strings, parts):
    answer = ''
    for i,j in zip(my_strings,parts):
        a= j[0]
        b= j[1]+1
        answer += i[a:b]
        
    return answer