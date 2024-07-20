def solution(myStr):
    temp = myStr.replace("a"," ").replace("b"," ").replace("c"," ").split(" ")
    answer = [x for x in temp if x != ""]
    if answer == []:
        return ["EMPTY"]
    return answer