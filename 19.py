from functools import cache
from os import path
from collections import deque

def part1():
    patterns = set()
    designs = []

    with open(path.join(path.dirname(__file__), "a19.txt")) as f:
        for line in f:
            if not patterns:
                patterns = {p.strip() for p in line.strip().split(',')}
            elif line.strip():
                designs.append(line.strip())
                
    count = 0
    for design in designs:
        stack = deque([design])
        possible = False
        while stack:
            curr = stack.pop()

            if not curr:
                possible = True
                break

            for i in range(len(curr)):
                if curr[:i+1] in patterns:
                    stack.append(curr[i+1:])

        if possible:
            count += 1
    print(count)

def part2():
    patterns = set()
    designs = []

    with open(path.join(path.dirname(__file__), "a19.txt")) as f:
        for line in f:
            if not patterns:
                patterns = {p.strip() for p in line.strip().split(',')}
            elif line.strip():
                designs.append(line.strip())
    
    @cache
    def search(design):
        if not design:
            return 1

        counts = 0
        for i in range(len(design)):
            if design[:i+1] in patterns:
                counts += search(design[i+1:])
        return counts

    res = 0
    for design in designs:
        res += search(design)
    print(res)


part1()
part2()