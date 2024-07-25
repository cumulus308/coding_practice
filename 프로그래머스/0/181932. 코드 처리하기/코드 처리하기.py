def solution(code):
    mode = 0
    ret = ""
    for i in range(len(code)):
        if mode == 0:
            if code[i] == '1':
                mode = 1
            if i % 2 == 0 and code[i] != '1':
                ret += code[i]
        elif mode == 1:
            if code[i] == '1':
                mode = 0
            if i % 2 == 1 and code[i] != '1':
                ret += code[i]
        
                
    return ret or "EMPTY"