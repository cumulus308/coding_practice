def count_trailing_zeros(n):
    count = 0
    i = 5
    while i <= n:
        count += n // i
        i *= 5
    return count

N = int(input())

print(count_trailing_zeros(N))