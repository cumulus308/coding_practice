def solution(hp):
    a = 0
    for i in [5,3,1]:
        b,hp = divmod(hp,i)
        a += b
    return a