def solution(order):
    clap = 0
    for i in str(order):
        if i in '369':
            clap += 1
    
    return clap