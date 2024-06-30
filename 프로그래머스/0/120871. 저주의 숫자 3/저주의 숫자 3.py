def solution(n):
    a = [x for x in range(200) if x % 3 != 0 and '3' not in str(x)]

    return a[n-1]