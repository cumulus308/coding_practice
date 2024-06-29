def solution(spell, dic):
    
    for i in dic:
        count=0
        for j in spell:
            if j not in i:
                break
            count += 1
            if count == len(spell):
                return 1
    return 2
    