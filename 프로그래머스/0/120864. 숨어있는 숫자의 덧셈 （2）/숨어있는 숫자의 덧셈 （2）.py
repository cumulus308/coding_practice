def solution(my_string):
    a = my_string.lower()
    for i in a:
        if i.isalpha():
            a = a.replace(i," ")
    reult = a.split()
    
    
    
    
    
    return sum(int(x) for x in reult )