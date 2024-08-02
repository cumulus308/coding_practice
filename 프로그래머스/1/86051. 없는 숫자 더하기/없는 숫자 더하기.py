def solution(numbers):
    answer = set(range(0,10))-set(numbers)

    return sum(answer)