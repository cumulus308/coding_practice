import sys

numbers = list(map(int, sys.stdin.read().split()))

result = [(numbers[i], numbers[i+1]) for i in range(1, len(numbers), 2)]

result.sort(key=lambda x: (x[0], x[1]))

sys.stdout.write("\n".join(f"{x} {y}" for x, y in result) + "\n")