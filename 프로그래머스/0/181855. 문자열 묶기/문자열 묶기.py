def solution(strArr):
    length_count = {}
    for s in strArr:
        length = len(s)
        if length in length_count:
            length_count[length] += 1
        else:
            length_count[length] = 1
    return max(length_count.values())