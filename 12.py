
from os import path

dirs = [(1,0), (-1,0), (0, 1), (0,-1)]

with open(path.join(path.dirname(__file__), "a12.txt")) as f:
    grid = {(x, y): val for y, line in enumerate(f.read().split('\n')) for x, val in enumerate(list(line))}

max_x = max([x[0] for x in grid.keys()])
max_y = max([x[1] for x in grid.keys()])

def in_bounds(pos):
    return pos[0] >= 0 and pos[0] <= max_x and pos[1] >= 0 and pos[1] <= max_y

def next(curr_pos, dir):
    return (curr_pos[0] + dir[0], curr_pos[1] + dir[1])

def part1():
    seen = set()

    def search(pos):
        if pos in seen:
            return (0, 0)
        
        seen.add(pos)
        area = 1
        boundary = 0

        for dir in dirs:
            next_pos = next(pos, dir)
            if in_bounds(next_pos):
                if grid[next_pos] == grid[pos]:
                    a, b = search(next_pos)
                    area += a
                    boundary += b
                else:
                    boundary += 1
            else:
                boundary += 1
        
        return (area, boundary)

    price = 0
    for pos, val in grid.items():
        if pos in seen:
            continue

        area, boundary = search(pos)
        price += area * boundary
    print(price)


def part2():
    seen = set()

    def search(pos):
        if pos in seen:
            return (0, 0)
        
        seen.add(pos)
        area = 1
        corners = 0

        for dir in dirs:
            next_pos = next(pos, dir)
            if in_bounds(next_pos):
                if grid[next_pos] == grid[pos]:
                    a, b = search(next_pos)
                    area += a
                    corners += b
        
        left = next(pos, (-1, 0))
        top = next(pos, (0, -1))
        right = next(pos, (1, 0))
        bottom = next(pos, (0, 1))

        # if the 2 neighbors are not part of the area, then it's a corner
        if (not in_bounds(left) or grid[left] != grid[pos]) and (not in_bounds(top) or grid[top] != grid[pos]):
            corners += 1
        
        if (not in_bounds(right) or grid[right] != grid[pos]) and (not in_bounds(top) or grid[top] != grid[pos]):
            corners += 1

        if (not in_bounds(right) or grid[right] != grid[pos]) and (not in_bounds(bottom) or grid[bottom] != grid[pos]):
            corners += 1

        if (not in_bounds(left) or grid[left] != grid[pos]) and (not in_bounds(bottom) or grid[bottom] != grid[pos]):
            corners += 1

        # if the 2 neighbors are part of the same area, then it's a corner if the diag is not part of the same area
        if in_bounds(left) and in_bounds(top) and grid[left] == grid[top] == grid[pos] and grid[pos] != grid[(pos[0] - 1, pos[1] - 1)]:
            corners += 1

        if in_bounds(right) and in_bounds(top) and grid[right] == grid[top] == grid[pos] and grid[pos] != grid[(pos[0] + 1, pos[1] - 1)]:
            corners += 1

        if in_bounds(right) and in_bounds(bottom) and grid[right] == grid[bottom] == grid[pos] and grid[pos] != grid[(pos[0] + 1, pos[1] + 1)]:
            corners += 1

        if in_bounds(left) and in_bounds(bottom) and grid[left] == grid[bottom] == grid[pos] and grid[pos] != grid[(pos[0] - 1, pos[1] + 1)]:
            corners += 1
        
        return (area, corners)

    price = 0
    for pos, val in grid.items():
        if pos in seen:
            continue

        area, corners = search(pos)
        price += area * corners
    print(price)

part1()
part2()