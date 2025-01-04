from functools import reduce
from math import floor
from os import path
import re

max_x=101
max_y=103
steps=100

def grid():
    return [[' ' for x in range(max_x)] for y in range(max_y)]

class Robot:
    def __init__(self, start_location, velocity):
        self.velocity = velocity
        self.location = start_location

    def __repr__(self):
        return f"\nlocation={self.location} velocity={self.velocity}"
    def __str__(self):
        return f"\nlocation={self.location} velocity={self.velocity}"

    def move(self):
        new_x = (self.location[0] + self.velocity[0]) % max_x
        new_y = (self.location[1] + self.velocity[1]) % max_y
        self.location = (new_x, new_y)
    
def part1():
    robots = []
    with open(path.join(path.dirname(__file__), "a14.txt")) as f:
        r = re.compile(r'p=(?P<x>-?\w+),(?P<y>-?\w+) v=(?P<vx>-?\w+),(?P<vy>-?\w+)')
        for line in f:
            x = r.search(line.strip())
            robots.append(
                Robot((int(x.group('x')), int(x.group('y'))), (int(x.group('vx')), int(x.group('vy')))))


    for i in range(steps):
        for r in robots:
            r.move()

    quadrants=[0, 0, 0, 0]
    mid_x = floor(max_x/2)
    mid_y = floor(max_y/2)
    for r in robots:
        if r.location[0] < mid_x and r.location[1] < mid_y:
            quadrants[0] += 1
        elif r.location[0] > mid_x and r.location[1] < mid_y:
            quadrants[1] += 1
        elif r.location[0] > mid_x and r.location[1] > mid_y:
            quadrants[2] += 1
        elif r.location[0] < mid_x and r.location[1] > mid_y:
            quadrants[3] += 1
    print(reduce(lambda x, y: x * y, quadrants))
part1()

def print_grid(robots, i, f):
        f.write(f'\nstep {i+1}')
        g = grid()
        for r in robots:
            g[r.location[1]][r.location[0]] = 'X'
        for y in g:
            f.write('\n')
            for x in y:
                if x == 'X':
                    f.write(x)
                else:
                    f.write('-')

def part2():
    robots = []
    with open(path.join(path.dirname(__file__), "a14.txt")) as f:
        r = re.compile(r'p=(?P<x>-?\w+),(?P<y>-?\w+) v=(?P<vx>-?\w+),(?P<vy>-?\w+)')
        for line in f:
            x = r.search(line.strip())
            robots.append(
                Robot((int(x.group('x')), int(x.group('y'))), (int(x.group('vx')), int(x.group('vy')))))

    with open("output14.txt", "w") as f:
        for i in range(10000):
            for r in robots:
                r.move()
            print_grid(robots, i, f)

part2()