def solution(s):
    new_s = s.lower()
    num_p = 0
    num_y = 0
    for i in new_s:
        if i == 'p':
            num_p += 1
        elif i == 'y':
            num_y += 1
    
    
    answer = True if num_p == num_y else False
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.


    return answer