from os import path

def part1():
    moves = []
    rloc = (0, 0)
    walls = set()
    boxes = set()

    with open(path.join(path.dirname(__file__), "a15.txt")) as f:
        for y, line in enumerate(f):
            if '#' in line:
                for x, c in enumerate(line.strip()):
                    if c == '@': rloc = (x, y)
                    elif c == '#': walls.add((x, y))
                    elif c == 'O': boxes.add((x, y))
            elif line.strip() != '':
                for c in line.strip():
                    moves.append(c)

    def get_dir(move):
        match move:
            case '^':
                return (0, -1)
            case '>':
                return (1, 0)
            case 'v':
                return (0, 1)
            case '<':
                return (-1, 0)

    def get_next_loc(dir, loc):
        return (loc[0] + dir[0], loc[1] + dir[1])

    def can_move(dir):
        test_loc = get_next_loc(dir, rloc)
        while True:
            if test_loc in walls:
                return (False, None)
            elif test_loc in boxes:
                test_loc = get_next_loc(dir, test_loc)
                continue
            else:
                return (True, test_loc)

    for move in moves:
        d = get_dir(move)
        m, open_location = can_move(d)
        if m:
            rloc = get_next_loc(d, rloc)
            if rloc != open_location:
                boxes.remove(rloc)
                boxes.add(open_location)

    result = 0
    for box in boxes:
        result += (box[1] * 100) + box[0]
    print(result)


def part2():
    moves = []
    rloc = (0, 0)
    walls = set()
    boxes_left = set()
    boxes_right = set()

    with open(path.join(path.dirname(__file__), "a15.txt")) as f:
        for y, line in enumerate(f):
            if '#' in line:
                for x, c in enumerate(line.strip()):
                    if c == '@': rloc = (2*x, y)
                    elif c == '#':
                        walls.add((2*x, y))
                        walls.add((2*x + 1, y))
                    elif c == 'O':
                        boxes_left.add((2*x, y))
                        boxes_right.add((2*x + 1, y))
            elif line.strip() != '':
                for c in line.strip():
                    moves.append(c)

    def get_dir(move):
        match move:
            case '^':
                return (0, -1)
            case '>':
                return (1, 0)
            case 'v':
                return (0, 1)
            case '<':
                return (-1, 0)

    def get_next_loc(dir, loc):
        return (loc[0] + dir[0], loc[1] + dir[1])


    for move in moves:
        d = get_dir(move)

        def can_move():
            seen_boxes = set()
            stack = [get_next_loc(d, rloc)]
            while stack:
                l = stack.pop()
                if l in walls: return (False, seen_boxes)
                if l in seen_boxes: continue
                if l in boxes_left:
                    seen_boxes.add(l)
                    stack.append(get_next_loc(d, l))
                    stack.append((l[0]+1, l[1]))
                elif l in boxes_right:
                    seen_boxes.add(l)
                    stack.append(get_next_loc(d, l))
                    stack.append((l[0]-1, l[1]))
            return (True, seen_boxes)

        m, boxes_to_move = can_move()
        if m:
            rloc = get_next_loc(d, rloc)
            new_boxes_left = set() 
            new_boxes_right = set() 
            for bl in boxes_left:
                if bl in boxes_to_move:
                    new_boxes_left.add((bl[0]+d[0], bl[1]+d[1]))
                    new_boxes_right.add((bl[0]+d[0]+1, bl[1]+d[1]))
                else:
                    new_boxes_left.add(bl)
                    new_boxes_right.add((bl[0]+1, bl[1]))
            boxes_left = new_boxes_left    
            boxes_right = new_boxes_right
    
    result = 0
    for box in boxes_left:
        result += (box[1] * 100) + box[0]
    print(result)

    
part1()
part2()