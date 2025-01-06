from os import path
from heapq import heappop, heappush

def read():
    falling_bytes = []
    with open(path.join(path.dirname(__file__), "a18.txt")) as f:
        for line in f:
            x, y = line.strip().split(',')
            falling_bytes.append((int(x),int(y)))
    return falling_bytes

def part1():
    max_coord = 70
    num_fallen = 1024
    falling_bytes = read()
    corrupted = set()
    for i in range(num_fallen):
        corrupted.add(falling_bytes[i])
    
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    h = [(0, 0, 0)]
    visited = set()

    while h:
        steps, x, y = heappop(h)
        if x == y == max_coord:
            return steps
        
        if x < 0 or x > max_coord or y < 0 or y > max_coord:
            continue

        if (x, y) in visited or (x, y) in corrupted:
            continue

        visited.add((x, y))

        for d in dirs:
            heappush(h, (steps + 1, x + d[0], y + d[1]))
        
print(part1())


def part2():
    falling_bytes = read()
    max_coord = 70
    corrupted = set()
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    for i in range(len(falling_bytes)):
        corrupted.add(falling_bytes[i])
    
        h = [(0, 0, 0)]
        visited = set()

        found_exit = False
        while h:
            steps, x, y = heappop(h)
            if x == y == max_coord:
                found_exit = True
                break
            
            if x < 0 or x > max_coord or y < 0 or y > max_coord:
                continue

            if (x, y) in visited or (x, y) in corrupted:
                continue

            visited.add((x, y))

            for d in dirs:
                heappush(h, (steps + 1, x + d[0], y + d[1]))
        
        if not found_exit:
            return falling_bytes[i]
        
print(part2())