def solution(s):
    answer = 0
    num_dict = {
    'zero':'0',
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9' }
    
    for i in num_dict:
        if i in s:
            s = s.replace(i,num_dict[i])
    return int(s)
    