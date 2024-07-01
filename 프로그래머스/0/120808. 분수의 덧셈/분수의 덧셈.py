def solution(numer1, denom1, numer2, denom2):
    i = (numer1 *denom2+ denom1*numer2)
    j = denom1*denom2
    g = gcb(i,j)
    return  [i/g, j/g]
    
    
def gcb(a,b):
    while b>0:
        a, b = b, a%b
    return a
    
    