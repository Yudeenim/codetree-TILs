OFFSET = 1000                                       #첫 번째 직사각형 = 2, 두 번째 직사각형 = 1
MAX_R = 2000
min_x, min_y, max_x, max_y = 0, 0, 0, 0
arr = []

rects = [
    tuple(map(int, input().split()))
    for _ in range(2)
]

checked = [
    [0] * (MAX_R + 1)
    for _ in range(MAX_R + 1)
]

for i, (x1, y1, x2, y2) in enumerate(rects, start=1):
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET

    for x in range(x1, x2):
        for y in range(y1, y2):
            checked[x][y] = (i % 2) + 1

for x in range(0, MAX_R + 1):
    for y in range(0, MAX_R + 1):
        if checked[x][y] == 2:
            arr.append([x, y])

if arr:  # arr가 비어있지 않은 경우에만 min_x, min_y 설정
    min_x, min_y = min(arr, key = lambda point: (point[0], point[1]))
    max_x, max_y = max(arr, key = lambda point: (point[0], point[1]))
    print((max_x - min_x + 1) * (max_y - min_y + 1))