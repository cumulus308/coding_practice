# 수 정렬하기 2 # 2751번
import sys

__ = sys.stdin.read
data = __().split()
# N = int(data[0])
num_list = list(map(int, data[1:]))

num_list.sort()

sys.stdout.write("\n".join(map(str, num_list)) + "\n")
