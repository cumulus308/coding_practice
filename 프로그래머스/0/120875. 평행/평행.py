def solution(dots):
    a,b,c,d = dots
    return1 =(b[1]-a[1])/(b[0]-a[0]) ==(d[1]-c[1])/(d[0]-c[0])
    return2 =(c[1]-a[1])/(c[0]-a[0]) ==(d[1]-b[1])/(d[0]-b[0]) 
    return3 =(d[1]-a[1])/(d[0]-a[0]) ==(c[1]-b[1])/(c[0]-b[0])
    return 1 if return1 or return2 or return3 else 0 
        
    
    
    
    
    
    
    
    
    
#     if (b[1]-a[1])/(b[0]-a[0]) ==(d[1]-c[1])/(d[0]-c[0]):
#         return 1
#     elif (c[1]-a[1])/(c[0]-a[0]) ==(d[1]-b[1])/(d[0]-b[0]):
#         return 1
#     elif (d[1]-a[1])/(d[0]-a[0]) ==(c[1]-b[1])/(c[0]-b[0]):
#         return 1
#     else:
#         return 0
    