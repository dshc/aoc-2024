from os import path

m = []

with open(path.join(path.dirname(__file__), "a4.txt")) as f:
    for line in f:
        m.append(list(line.strip()))

max_y = len(m)
max_x = len(m[0])

def next_letter(curr):
    if curr == 'X': return 'M'
    if curr == 'M': return 'A'
    return 'S'

def search(x, y, letter, xx, yy) -> int:
    if x < 0 or x >= max_x or y < 0 or y >= max_y:
        return 0

    if m[y][x] != letter:
        return 0

    if letter == 'S':
        return 1
    
    return search(x+xx, y+yy, next_letter(letter), xx, yy)
    
result = 0
for y in range(max_y):
    for x in range(max_x):
        result += search(x, y, 'X', 1, 0)
        result += search(x, y, 'X', -1, 0)
        result += search(x, y, 'X', 0, 1)
        result += search(x, y, 'X', 0, -1)
        result += search(x, y, 'X', 1, 1)
        result += search(x, y, 'X', 1, -1)
        result += search(x, y, 'X', -1, 1)
        result += search(x, y, 'X', -1, -1)
print(result) # part 1

def search_2(x, y):
    if x < 0 or x >= max_x or y < 0 or y >= max_y:
        return 0

    if m[y][x] == 'M': return 1
    if m[y][x] == 'S': return 2
    return 0

result = 0
for y in range(max_y):
    for x in range(max_x):
        if m[y][x] == 'A':
            a = search_2(x+1, y+1) + search_2(x-1, y-1)
            b = search_2(x-1, y+1) + search_2(x+1, y-1)
            if a == 3 and b == 3:
                result += 1
print(result) # part 2