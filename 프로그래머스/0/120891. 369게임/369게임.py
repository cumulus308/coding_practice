def solution(order):
    clap = 0
    for i in str(order):
        if i in ['3','6','9']:
            clap += 1
    
    return clap