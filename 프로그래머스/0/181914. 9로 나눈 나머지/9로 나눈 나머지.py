def solution(number):
    answer = sum(int(x)for x in number)%9
    return answer