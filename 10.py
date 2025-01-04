from functools import cache
from os import path

dirs = [(1,0), (-1,0), (0, 1), (0,-1)]

with open(path.join(path.dirname(__file__), "a10.txt")) as f:
    grid = {(x, y): int(val) for y, line in enumerate(f.read().split('\n')) for x, val in enumerate(list(line))}

max_x = max([x[0] for x in grid.keys()])
max_y = max([x[1] for x in grid.keys()])

def in_bounds(pos):
    return pos[0] >= 0 and pos[0] <= max_x and pos[1] >= 0 and pos[1] <= max_y

trailheads = set()
for pos, val in grid.items():
    if val == 0: trailheads.add(pos)

def search(pos, peaks, use_peaks):
    if grid[pos] == 9:
        if use_peaks:
            if not pos in peaks:
                peaks.add(pos)
                return 1
        else:
            return 1
    res = 0
    for dir in dirs:
        next = (dir[0] + pos[0], dir[1] + pos[1])
        if in_bounds(next) and grid[next] == grid[pos]+1:
            res += search(next, peaks, use_peaks)
    return res

score = 0
score2 = 0
for trailhead in trailheads:
    score += search(trailhead, set(), True)
    score2 += search(trailhead, set(), False)
print(score) # part 1
print(score2) # part 2