from collections import Counter

def solution(a, b, c, d):
    dice = [a, b, c, d]
    counter = Counter(dice)
    count_values = list(counter.values())
    unique_values = list(counter.keys())
    
    if len(unique_values) == 1:
        return 1111 * dice[0]
    elif len(unique_values) == 2:
        if 3 in count_values:
            p = max(unique_values, key=counter.get)
            q = min(unique_values, key=counter.get)
            return (10 * p + q) ** 2
        else:
            return (unique_values[0] + unique_values[1]) * abs(unique_values[0] - unique_values[1])
    elif len(unique_values) == 3:
        for num in unique_values:
            if counter[num] == 2:
                unique_values.remove(num)
                break
        q, r = unique_values
        return q * r
    else:
        return min(dice)
