str = input()
a = "".join([i.lower() if i.isupper() else i.upper() for i in str])
print(a)
        
