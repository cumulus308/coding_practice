def solution(arr):
    answer = []
    for i in arr:
        if not answer:
            answer.append(i)
        if i !=answer[-1]:
            answer.append(i)
    return answer
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    return answer