def solution(intStrs, k, s, l):
    return [int(intstr[s:s+l]) for intstr in intStrs if int(intstr[s:s+l])>k]