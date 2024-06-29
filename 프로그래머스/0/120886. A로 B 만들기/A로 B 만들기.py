def solution(before, after):
    list_after = list(after)
    while list_after:
        for i in before:
            if i in list_after:
                list_after.remove(i)
            else:
                return 0
        else:
            return 1
            