a, b = input().split()
if a == b:
    print('==')
else:
    print(">" if int(a)>int(b) else '<')