def solution(lines):
    # 선분을 표시할 배열 생성 (좌표 범위: -100 ~ 100)
    array = [0] * 201
    
    # 각 선분에 대해 배열에 표시
    for line in lines:
        start, end = line
        for i in range(start + 100, end + 100):
            array[i] += 1
    
    # 2개 이상의 선분이 겹치는 부분의 길이 계산
    overlap_length = sum(1 for count in array if count >= 2)
    
    return overlap_length