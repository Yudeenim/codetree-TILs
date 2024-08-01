n, t = tuple(map(int, input().split()))
dirs = input()
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
x, y = n//2, n//2
curr_dir = 3
num_cnt = arr[x][y]

dxs = [0, 1, 0, -1]            #동, 남, 서, 북
dys = [1, 0, -1, 0]

for c_dir in dirs:
    if c_dir == 'L':
        curr_dir = (curr_dir - 1 + 4) % 4
    elif c_dir == 'R':
        curr_dir = (curr_dir + 1) % 4
    else:
        nx, ny = x + dxs[curr_dir], y + dys[curr_dir]
        if 0 <= nx < n and 0 <= ny < n:  # 이동 후 범위 체크
            x, y = nx, ny
            num_cnt += arr[x][y]

print(num_cnt)