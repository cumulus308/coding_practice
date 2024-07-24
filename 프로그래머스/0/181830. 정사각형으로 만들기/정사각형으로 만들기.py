def solution(arr):
#     max_len=max(len(arr),len(arr[0]))
#     for i in range(max_len):
#         arr[i] = arr[i] +([0]*(max_len-len(arr[i])))
#     return arr

    # 모든 행의 최대 길이와 전체 행 수 중 큰 값을 찾습니다
    max_len = max(max(len(row) for row in arr), len(arr))

    # 각 행을 max_len 길이로 확장하고, 필요한 만큼 새 행을 추가합니다
    result = [row + [0] * (max_len - len(row)) for row in arr]
    result += [[0] * max_len] * (max_len - len(result))

    return result