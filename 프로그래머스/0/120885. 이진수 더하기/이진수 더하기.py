def solution(bin1, bin2):
    total1 = []
    total2 = []
    for i,j in zip(range(len(bin1)), bin1[::-1]):
        total1.append((2**i)*int(j))
    for i,j in zip(range(len(bin2)), bin2[::-1]):
        total2.append((2**i)*int(j))
        answer = (sum(total1)+sum(total2))
    
    
    return bin(answer)[2:]