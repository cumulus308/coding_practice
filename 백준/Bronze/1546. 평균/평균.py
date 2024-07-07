# 과목 수 입력 받기
N = int(input())

# 점수들을 리스트로 입력 받기
scores = list(map(int, input().split()))

# 최고점 찾기
max_score = max(scores)

# 새로운 점수 계산 및 합계 구하기
new_sum = sum(score / max_score * 100 for score in scores)

# 새로운 평균 계산
new_average = new_sum / N

# 결과 출력 (소수점 둘째 자리까지)
print(f"{new_average:.2f}")