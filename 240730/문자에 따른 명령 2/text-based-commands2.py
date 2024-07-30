x, y = 0, 0
dirs = input()
curr_dir = 3

dxs = [1, 0, -1, 0]
dys = [0, -1, -, 1]

for c_dir in dirs:
    if c_dir == 'L':
        curr_dir = (curr_dir -1 + 4) % 4
    elif c_dir == 'R':
        curr_dir = (curr_dir + 1 + 4) % 4
    else:
        x, y = x + dxs[current_dir], y + dys[current_dir]

print(x, y)