hour, minute = input().split()
cooking_time = int(input())
hour, minute =int(hour), int(minute)
h, m = divmod(cooking_time,60)

hours = 0
minutes = 0

if m + minute >= 60:
    minutes = m + minute -60
    hours += 1
elif m + minute < 60:
    minutes = m + minute
if h + hour +hours>=24:
    hours = h + hour +hours -24
elif h + hour +hours<24:
    hours = h + hour +hours
    
print(hours, minutes)