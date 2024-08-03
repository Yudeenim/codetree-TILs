n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
result = -1

def in_grid (x, y, i, j):
    if x >= 0 and y >= 0 and x + j < m and y + i < n:
        return True
    else: return False

def is_pos (x, y, i, j):
    for k in range(j+1):
        for l in range(i+1):
            if grid[y+l][x+k] <= 0:
                return False
    return True


def simulation (x, y):
    global result
    for k in range(n):
        for l in range(m):
            if in_grid(x, y, k, l) and is_pos(x, y, k, l):
                result = max(result, (l+1)*(k+1))

for a in range(n):
    for b in range(m):
        simulation(b, a)

print(result)