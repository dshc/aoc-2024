from os import path

def part1():
    with open(path.join(path.dirname(__file__), "a6.txt")) as f:
        grid = {(x, y): val for y, line in enumerate(f.read().split('\n'))
            for x, val in enumerate(line)}

    pos = (0, 0)
    dir = '^'
    for k, v in grid.items():
        if v == '^':
            pos = k

    def turn(d):
        if d == '^':
            return '>'
        if d == '>':
            return 'v'
        if d == 'v':
            return '<'
        return '^'

    def check_pos(p):
        if not p in grid or (grid[p] == '.' or grid[p] == '^'):
            return True
        return False

    visited = set()
    while True:
        if not pos in grid:
            break

        visited.add(pos)
        x, y = pos

        if dir == '^':
            if check_pos((x, y-1)):
                pos = (x, y-1)
            else:
                dir = turn(dir)
        elif dir == '>':
            if check_pos((x+1, y)):
                pos = (x+1, y)
            else:
                dir = turn(dir)
        elif dir == 'v':
            if check_pos((x, y+1)):
                pos = (x, y+1)
            else:
                dir = turn(dir)
        elif dir == '<':
            if check_pos((x-1, y)):
                pos = (x-1, y)
            else:
                dir = turn(dir)

    print(len(visited)) # part 1

def part2():
    with open(path.join(path.dirname(__file__), "a6.txt")) as f:
        grid = {(x, y): val for y, line in enumerate(f.read().split('\n'))
            for x, val in enumerate(line)}
    
    count = 0

    starting_pos = (0, 0)
    for k, v in grid.items():
        if v == '^':
            starting_pos = k

    for k, v in grid.items():
        if v == '#' or v == '^':
            continue

        # create temp grid
        test_grid = grid.copy()
        test_grid[k] = '#'

        dir = '^'
        pos = starting_pos
        def turn(d):
            if d == '^':
                return '>'
            if d == '>':
                return 'v'
            if d == 'v':
                return '<'
            return '^'

        def check_pos(p):
            if not p in test_grid or (test_grid[p] == '.' or test_grid[p] == '^'):
                return True
            return False

        visited = set()
        while True:
            if not pos in test_grid:
                break

            if (pos, dir) in visited:
                count += 1
                break

            visited.add((pos, dir))
            x, y = pos

            if dir == '^':
                if check_pos((x, y-1)):
                    pos = (x, y-1)
                else:
                    dir = turn(dir)
            elif dir == '>':
                if check_pos((x+1, y)):
                    pos = (x+1, y)
                else:
                    dir = turn(dir)
            elif dir == 'v':
                if check_pos((x, y+1)):
                    pos = (x, y+1)
                else:
                    dir = turn(dir)
            elif dir == '<':
                if check_pos((x-1, y)):
                    pos = (x-1, y)
                else:
                    dir = turn(dir)
    print(count) # part 2


part1()
part2()