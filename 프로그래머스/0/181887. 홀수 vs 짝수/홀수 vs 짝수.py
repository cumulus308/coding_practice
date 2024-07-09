def solution(num_list):
    a = sum([x for x in num_list[::2]])
    b = sum([y for y in num_list[1::2]])
    return max(a,b)