def solution(my_string):
    ss = []
    for i in my_string:
        if i.isupper():
            ss.append(i.lower())
        elif i.islower:
            ss.append(i.upper())
    return "".join(ss)