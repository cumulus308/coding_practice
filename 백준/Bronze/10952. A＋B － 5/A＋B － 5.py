while True:
    a= input()
    if a != "0 0":
        b,c= map(int,a.split())
        print(b+c)
    else:
        break