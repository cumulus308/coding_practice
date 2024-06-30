def solution(dots):
    w = []
    h = []
    for i in dots:
        w.append(i[0])
        h.append(i[1])
        
    fw = max(w) - min(w)
    fh = max(h) - min(h)
    return fw * fh
