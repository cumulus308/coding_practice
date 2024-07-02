def solution(price):
    dic = {
        500_000: 0.8,
        300_000: 0.9,
        100_000: 0.95,
        0: 1
    }
    return int(price * next(y for x, y in dic.items() if price >= x))