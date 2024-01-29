OFFSET = 100000
MAX_R = 200000

# 변수 선언 및 입력
n = int(input())
moves = [
    list(input().split())
    for _ in range(n)
]
moved = []
colors = [0] * (MAX_R + 1)
cnt_white, cnt_black = 0, 0
cur = OFFSET

for i, (distance, direction) in enumerate(moves, start=1):
    distance = int(distance)

    if direction == 'L':
        moved.append(-distance)
    else:
        moved.append(distance)

for index, k in enumerate(moved):
    if index == 0:
        if k >= 0:
            for j in range(cur, cur + k):
                colors[j] = "Black"
            cur = cur + k
            continue
        elif k < 0:
            for j in range(cur + k, cur):
                colors[j] = "White"
            cur = cur + k
            continue

    if k >= 0 and moved[index-1] <0:
        for j in range(cur, cur + k):
            colors[j] = "Black"
        cur = cur + k

    elif k >= 0 and moved[index-1] >= 0:
        for j in range(cur, cur + k - 1):
            colors[j] = "Black"
        cur = cur + k - 1

    elif k < 0 and moved[index-1] >= 0:
        for j in range(cur + k, cur):
            colors[j] = "White"
        cur = cur + k

    elif k < 0 and moved[index-1] < 0:
        for j in range(cur + k + 1, cur):
            colors[j] = "White"
        cur = cur + k + 1

for elem in colors:
    if elem == "White":
        cnt_white += 1
    elif elem == "Black":
        cnt_black += 1

print(cnt_white, cnt_black)