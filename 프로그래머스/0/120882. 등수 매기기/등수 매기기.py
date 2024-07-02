def solution(score):
    avg_score = [sum(x)/2 for x in score]
    sorted_score = sorted(avg_score,reverse = True) 
    return [sorted_score.index(s) + 1 for s in avg_score]