from collections import defaultdict
from os import path

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def find_antinodes(a, b):
    diff_x = abs(a[0] - b[0])
    diff_y = abs(a[1] - b[1])
    ax = a[0]
    ay = a[1]
    bx = b[0]
    by = b[1]

    if a[0] < b[0]:
        ax -= diff_x
        bx += diff_x
    elif a[0] > b[0]:
        ax += diff_x
        bx -= diff_x

    if a[1] < b[1]:
        ay -= diff_y
        by += diff_y
    elif a[1] > b[1]:
        ay += diff_y
        by -= diff_y
    
    return [(ax, ay), (bx, by)]

with open(path.join(path.dirname(__file__), "a8.txt")) as f:
    grid = {(x, y): val for y, line in enumerate(f.read().split('\n')) for x, val in enumerate(line)}

max_x = max([x for x,y in grid])
max_y  = max([y for x,y in grid])

# find all unique pairs of positions with the same antenna
antennas = defaultdict(list)
for k, v in grid.items():
    if v == '.': continue
    antennas[v].append(k)

antinodes = set()
for _, a in antennas.items():
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            for antinode in find_antinodes(a[i], a[j]):
                antinodes.add(antinode)

print(sum(a[0] >= 0 and a[0] <= max_x and a[1] >= 0 and a[1] <= max_y for a in antinodes)) # part 1

def find_antinodes2(a, b):
    antinodes = []
    diff_x = a[0] - b[0]
    diff_y = a[1] - b[1]

    tmp = (a[0], a[1])
    while tmp[0] >= 0 and tmp[0] <= max_x and tmp[1] >= 0 and tmp[1] <= max_y:
        antinodes.append(tmp)
        tmp = (tmp[0] + diff_x, tmp[1] + diff_y)

    tmp = (a[0], a[1])
    while tmp[0] >= 0 and tmp[0] <= max_x and tmp[1] >= 0 and tmp[1] <= max_y:
        antinodes.append(tmp)
        tmp = (tmp[0] - diff_x, tmp[1] - diff_y)
    
    return antinodes
    

antinodes2 = set()
for _, a in antennas.items():
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            for antinode in find_antinodes2(a[i], a[j]):
                antinodes2.add(antinode)

print(len(antinodes2))
