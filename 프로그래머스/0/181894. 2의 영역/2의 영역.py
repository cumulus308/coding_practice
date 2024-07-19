def solution(arr):
    if 2 not in arr:
        return [-1]
    number_2 = list(filter(lambda x : arr[x]==2,range(len(arr))))
    left = number_2[0]
    right = number_2[-1]
    
    return arr[left:right+1]