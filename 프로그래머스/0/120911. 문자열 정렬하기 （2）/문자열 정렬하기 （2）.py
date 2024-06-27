def solution(my_string):
    a = list(my_string.lower())
    a.sort()
    b ="".join(a)
    return "".join(a)