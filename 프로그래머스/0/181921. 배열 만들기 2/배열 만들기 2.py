def solution(l, r):
    answer = []
    
    # 0부터 999999까지 모든 수를 검사
    for num in range(1000000):
        # 숫자를 문자열로 변환
        str_num = str(num)
        
        # 숫자가 0과 5로만 이루어져 있는지 확인
        if all(digit in '05' for digit in str_num):
            # 범위 내에 있는지 확인
            if l <= num <= r:
                answer.append(num)
            # r을 초과하면 반복 중단
            elif num > r:
                break
    
    # 결과가 없으면 [-1] 반환
    return answer if answer else [-1]