def solution(myString):
    a = myString
    for i in a:
        if ord(str(i))< ord("l"):
            a = a.replace(i,'l')

    return a