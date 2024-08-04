n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def get_max_time(n, grid):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def next_direction(current_dir, cell_value):
        if cell_value == 1:  # /
            return (3, 2, 1, 0)[current_dir]
        elif cell_value == 2:  # \
            return (1, 0, 3, 2)[current_dir]
        return current_dir
    
    def simulate(start_x, start_y, direction):
        x, y, dir = start_x, start_y, direction
        time = 0
        while 0 <= x < n and 0 <= y < n:
            time += 1
            dx, dy = directions[dir]
            x, y = x + dx, y + dy
            if 0 <= x < n and 0 <= y < n:
                dir = next_direction(dir, grid[x][y])
        return time + 1

    max_time = 0
    for i in range(n):
        max_time = max(max_time, simulate(0, i, 1))  
        max_time = max(max_time, simulate(n - 1, i, 3)) 
        max_time = max(max_time, simulate(i, 0, 0))  
        max_time = max(max_time, simulate(i, n - 1, 2)) 
    return max_time

print(get_max_time(n, grid))