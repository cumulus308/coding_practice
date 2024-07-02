def solution(my_string):
    return sorted(int(x) for x in my_string if x.isdigit())


# def solution(my_string):
#     answer = []
#     for i in my_string:
#         if i.isdigit():
#             answer.append(int(i))
#     return sorted(answer)