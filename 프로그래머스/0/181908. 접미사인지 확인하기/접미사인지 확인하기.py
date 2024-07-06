def solution(my_string, is_suffix):
    answer = 0
    return int(my_string[-(len(is_suffix)):] == is_suffix)