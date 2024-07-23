def solution(arr):
    def transform(num):
        if num >= 50 and num % 2 == 0:
            return num // 2
        elif num < 50 and num % 2 == 1:
            return num * 2 + 1
        return num

    def iterate(arr):
        return [transform(num) for num in arr]

    x = 0
    prev = arr
    while True:
        next_arr = iterate(prev)
        if prev == next_arr:
            return x
        prev = next_arr
        x += 1