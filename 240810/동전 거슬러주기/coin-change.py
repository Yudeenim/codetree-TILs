MAX_ANS = 10001

n, m = tuple(map(int, input().split()))

coin = [0] + list(map(int, input().split()))

dp = [MAX_ANS for _ in range(m + 1)]

dp[0] = 0

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if i >= coin[j]:
            dp[i] = min(dp[i], dp[i - coin[j]] + 1)

min_cnt = dp[m]

if min_cnt == MAX_ANS:
    min_cnt = -1

print(min_cnt)