def solution(arr, flag):
    X = []
    for i in range(len(arr)):
        if flag[i]:
            X.extend([arr[i]] * (arr[i] * 2))
        else:
            X = X[:-arr[i]] if arr[i] <= len(X) else []
    return X