n, t = tuple(map(int, input().split()))
r, c, d = tuple(input().split())
r = int(r) - 1
c = int(c) - 1

direction = {
    'R' : 0,
    'D' : 1,
    'U' : 2,
    'L' : 3
}

move_dir = direction[d]
drs = [0, 1, -1, 0]
dcs = [1, 0, 0, -1]

def in_range (r, c):
    return 0 <= r and r < n and 0 <= c and c < n

while (t > 0):
    if in_range(r, c):
        nr, nc = r + drs[move_dir], c + dcs[move_dir]
        if nr < 0 or nc < 0:
            nr, nc = r, c
            move_dir = 3 - move_dir
        r, c = nr, nc                          
    else:
        move_dir = 3 - move_dir
    t -= 1

print(r+1, c+1)