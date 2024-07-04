def solution(myString, pat):
    # myString의 "A"를 "B"로, "B"를 "A"로 바꾸는 함수
    def swap_ab(s):
        return ''.join('B' if c == 'A' else 'A' for c in s)
    
    # myString을 변환
    swapped = swap_ab(myString)
    
    # 변환된 문자열에 pat이 포함되어 있는지 확인
    return 1 if pat in swapped else 0