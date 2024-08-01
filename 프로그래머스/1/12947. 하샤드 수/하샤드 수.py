def solution(x):
    sum_x = sum(int(i) for i in str(x))
    return False if x%sum_x else True