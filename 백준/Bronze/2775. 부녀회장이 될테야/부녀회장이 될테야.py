# 부녀회장이 될꺼야 # 2775번
def calculate_people(k, n):
    # 각 층과 호수를 기록할 배열 생성
    dp = [[0] * (n+1) for _ in range(k+1)]
    
    # 0층의 값을 초기화
    for i in range(1, n+1):
        dp[0][i] = i
    
    # DP를 이용해 각 층의 값을 계산
    for i in range(1, k+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
    
    return dp[k][n]

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    print(calculate_people(k, n))
