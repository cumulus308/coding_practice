while True:
    numbers = list(map(int, input().split()))
    numbers.sort()
    a,b,c = numbers
    if a == 0 and b == 0 and c ==0:
        break
    else:
        if a**2 +b**2 == c**2:
            print("right")
        else:
            print("wrong")
            