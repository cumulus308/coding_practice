def solution(sides):
    return len([x for x in range(abs(sides[1]-sides[0])+1,sum(sides))])