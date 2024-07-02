def solution(num_list):
    answer = [0,0]
    for i in num_list:
        answer[i%2]+=1
    return answer


# def solution(num_list):
#     even = len([x for x in num_list if x %2 ==0])
#     odd = len([x for x in num_list if x %2 !=0])
#     return (even, odd)