def solution(chicken):
    result = 0
    coupon = 0
    coupon = chicken
    
    while coupon >=10:
        a= coupon // 10
        result += a
        coupon -= 10 * (a)
        coupon += a
    return result
