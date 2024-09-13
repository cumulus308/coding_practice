def solution(numbers, direction):
    if direction == "right":
        answer = [numbers.pop()] + numbers
    elif direction == "left":
        value = numbers.pop(0)
        answer = numbers +[value]
    return answer