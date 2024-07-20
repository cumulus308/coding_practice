def solution(myString, pat):
    pat_len = len(pat)
    for i in range(len(myString)):
        a = myString[len(myString)-(i + pat_len):len(myString)-i]
        if a == pat:
            return myString[:len(myString)-i]