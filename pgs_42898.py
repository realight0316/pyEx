# 프로그래머스 : 등굣길 (https://programmers.co.kr/learn/courses/30/lessons/42898)

# 문제 설명
# 계속되는 폭우로 일부 지역이 물에 잠겼습니다. 물에 잠기지 않은 지역을 통해 학교를 가려고 합니다. 
# 집에서 학교까지 가는 길은 m x n 크기의 격자모양으로 나타낼 수 있습니다.

# 가장 왼쪽 위, 즉 집이 있는 곳의 좌표는 (1, 1)로 나타내고 가장 오른쪽 아래, 
# 즉 학교가 있는 곳의 좌표는 (m, n)으로 나타냅니다.

# 격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다. 
# 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 
# 1,000,000,007로 나눈 나머지를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 격자의 크기 m, n은 1 이상 100 이하인 자연수입니다.
# m과 n이 모두 1인 경우는 입력으로 주어지지 않습니다.
# 물에 잠긴 지역은 0개 이상 10개 이하입니다.
# 집과 학교가 물에 잠긴 경우는 입력으로 주어지지 않습니다.

# 입출력 예
# m	n	puddles	return
# 4	3	[[2, 2]]	4


def solution(m, n, puddles):
    area = [[1 for _ in range(m+1)]for _ in range(n+1)]     # 지도 생성
    dp   = [[0 for _ in range(m+1)]for _ in range(n+1)]     # dp 메모리 생성

    for p1,p2 in puddles:                                   # 침수지역 지도에 기입
        area[p2][p1] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if area[i][j] != 0:                             # 침수지역 피해서 이동
                if i==1 and j==1:                           # 시작지점을 1로 기입
                    dp[i][j] = 1
                    continue
                else:                                       # 오른쪽, 아래로만 움직이므로
                    dp[i][j] += dp[i-1][j] + dp[i][j-1]     # 현위치 기준 상,좌의 합을 현위치에 기입
    for q in dp:
        print(q)

    return dp[n][m] % 1000000007                            # 출력조건에 맞게 나누기 연산

m= 4; n= 3;puddles= [[2,2]]
print(solution(m,n,puddles))