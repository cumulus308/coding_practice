def solution(price, money, count):
    total_price = (count*(2*price +(count-1)*price))/2
    return max(total_price-money,0)