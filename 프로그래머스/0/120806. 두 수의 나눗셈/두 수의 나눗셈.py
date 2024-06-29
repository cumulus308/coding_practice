def solution(num1, num2):
    a = str(num1 / num2 * 1000)
    answer = int(a.split(".")[0])
    return answer