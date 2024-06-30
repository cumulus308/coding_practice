def solution(num, total):
    k = (total - ((num*(num-1))//2))//num
    sum_list = [k + x for x in range(num)]
        
    return sum_list