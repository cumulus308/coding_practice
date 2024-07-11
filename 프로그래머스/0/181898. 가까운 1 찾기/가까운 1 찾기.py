def solution(arr, idx):
    answer = 0
    for i in range(len(arr[idx:])):
        if arr[idx+i] == 1:
            return idx+i
    return -1