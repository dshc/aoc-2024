from os import path

with open(path.join(path.dirname(__file__), "a9.txt")) as f:
    disk = [int(x) for x in list(f.read().strip())]

def part1():
    # filled - array with pairs of (index: fileId)
    # free - array of indices with free space
    index = 0
    filled = []
    free = []
    file_id = 0
    for x in [disk[i:i+2] for i in range(0, len(disk), 2)]:
        for _ in range(x[0]):
            filled.append((index, file_id))
            index += 1

        if len(x) > 1:
            for _ in range(x[1]):
                free.append(index)
                index += 1

        file_id += 1

    max_index = len(filled) - 1 # this represents the max index we want to fill up to
    tmp = []
    for i in free:
        if i > max_index: break
        last = filled.pop()
        tmp.append((i, last[1]))

    filled.extend(tmp)

    print(sum([a*b for a, b in filled])) # part 1

def part2():
    files = {} # file id: (file size, starting index)
    current_idx = 0
    current_file_id = 0
    free = [] # (size, starting index)
    for x in [disk[i:i+2] for i in range(0, len(disk), 2)]:
        files[current_file_id] = (x[0], current_idx)
        current_file_id += 1
        current_idx += x[0]
        if len(x) > 1 and x[1] > 0:
            free.append((x[1], current_idx))
            current_idx += x[1]

    for i in range(current_file_id - 1, -1, -1):
        file = files[i]
        for j in range(len(free)):
            # if the free item is to the right of the file already, forget it
            if free[j][1] >= file[1]:
                break

            if free[j][0] >= file[0]:
                # file fits!
                files[i] = (file[0], free[j][1])
                free[j] = (free[j][0] - file[0], free[j][1] + file[0])
                break
    
    res = 0
    for file_id, v in files.items():
        file_size, starting_idx = v
        for x in range(starting_idx, starting_idx + file_size):
            res += (x * file_id)
    print(res)

# part1()
part2()