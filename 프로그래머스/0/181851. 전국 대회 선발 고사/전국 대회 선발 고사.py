def solution(rank, attendance):
    student = [(r,i) for i,(r,a) in enumerate(zip(rank, attendance)) if a]
    student.sort()
    
    a, b, c = [i for _,i in student[:3]]
    return 10000*a + 100 *b + c