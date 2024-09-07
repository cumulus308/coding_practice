# 달팽이는 올라가고 싶다. 2869번
A, B, V = map(int, input().split())

hight = V-A
one_day_up = A - B
result = hight // one_day_up if hight % one_day_up == 0 else hight // one_day_up + 1
    
print(result + 1)