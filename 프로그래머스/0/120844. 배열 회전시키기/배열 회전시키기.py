def solution(numbers, direction):
    num = len(numbers)
    return (numbers*2)[num-1:2*num-1] if direction == "right" else(numbers*2)[1:num+1]