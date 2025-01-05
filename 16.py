from collections import deque
from os import path
from heapq import heappush, heappop

start = None
end = None
walls = set()
with open(path.join(path.dirname(__file__), "a16.txt")) as f:
    for y, line in enumerate(f):
        for x, c in enumerate(line.strip()):
            if c == 'S': start = (x,y)
            elif c == 'E': end = (x,y)
            elif c == '#': walls.add((x,y))

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = dict()
heap = [(0, start, 0)]

end_score = None
while heap:
    score, loc, idir = heappop(heap)
    if loc == end:
        end_score = score
        break
    
    if loc in walls:
        continue

    if (loc, idir) in visited and visited[(loc, idir)] < score:
        continue

    visited[(loc, idir)] = score

    for i in range(len(dirs)):
        next_dir = dirs[i]
        next_loc = (next_dir[0] + loc[0], next_dir[1] + loc[1])
        if idir == i:
            heappush(heap, (score + 1, next_loc, i))
        else:
            heappush(heap, (score + 1001, next_loc, i))

print(end_score)