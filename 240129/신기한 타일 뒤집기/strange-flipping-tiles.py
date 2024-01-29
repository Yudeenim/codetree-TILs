OFFSET = 100000    # 흰색은 2, 검은색은 1
MAX_R = 200000

n = int(input())
colors = [0] * (MAX_R + 1)
cur = MAX_R // 2
cnt_white = 0
cnt_black = 0

for _ in range(n):
    distance, direction = tuple(input().split())
    distance = int(distance)

    if direction == 'L':
        # 왼쪽으로 이동할 경우: colors의 cur(현재 상태)를 기준으로 왼쪽으로 distance만큼 0을 2로 변경
        for i in range(cur, cur - distance, -1):
            colors[i] = 2
        cur -= distance

    else:
        # 오른쪽으로 이동할 경우: colors의 cur(현재 상태)를 기준으로 오른쪽으로 distance만큼 0을 1로 변경
        for i in range(cur, cur + distance, 1):
            colors[i] = 1
        cur += distance

for elem in colors:
    if elem == 2:
        cnt_white += 1
    elif elem == 1:
        cnt_black += 1

if cnt_black == 0:
    print(cnt_white - 1, 0)
elif cnt_white == 0:
    print(0, cnt_black - 1)
else: print(cnt_white, cnt_black)