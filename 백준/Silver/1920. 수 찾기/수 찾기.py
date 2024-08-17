import sys
from bisect import bisect_left

def binary_search(arr, x):
    i = bisect_left(arr, x)
    return i != len(arr) and arr[i] == x

input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
queries = list(map(int, input().split()))

result = ['1' if binary_search(A, x) else '0' for x in queries]
sys.stdout.write('\n'.join(result))