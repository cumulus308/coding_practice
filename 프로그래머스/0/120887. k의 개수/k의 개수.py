def solution(i, j, k):
    count = 0
    for n in range(i,j+1):
        for m in str(n):
            if m == str(k):
                count += 1
    return count