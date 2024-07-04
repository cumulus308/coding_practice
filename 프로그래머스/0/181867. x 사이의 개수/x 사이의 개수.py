def solution(myString):
    answer = []
    a = myString.split("x")
    for i in a:
        answer.append(len(i))
    return answer
    # return [ len(i) for i in myString.split('x')]