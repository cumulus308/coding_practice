hour, minute = input().split()
hour, minute =int(hour), int(minute)
if minute >=45:
    print(hour,minute-45)
elif hour>=1 and minute <45:
    print(hour-1, minute+15)
elif hour< 1 and minute <45:
    print(23, minute+15)
