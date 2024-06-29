def solution(box, n):
    did_width =box[0] // n
    did_height = box[1] // n
    did_high = box[2] // n
    
    answer = did_width * did_height * did_high
    return answer