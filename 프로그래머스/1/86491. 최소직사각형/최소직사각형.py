def solution(sizes):
    answer = 0
    for i in sizes:
        if i[1] > i[0]:
            i[1], i[0] = i[0], i[1]
    a = max(x[0] for x in sizes)
    b = max(x[1] for x in sizes)
    return a * b