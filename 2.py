from os import path

def is_safe(prev, curr, increasing):
    if prev == curr or (increasing and prev > curr) or (not increasing and prev < curr) or abs(prev - curr) > 3:
        return False
    return True

def part1():
    res = 0
    with open(path.join(path.dirname(__file__), "a2.txt")) as f:
        for line in f:
            s = list(map(int, line.split()))
            increasing = s[0] < s[-1]
            safe = True
            for prev, curr in zip(s, s[1:]):
                safe &= is_safe(prev, curr, increasing)
            res += 1 if safe else 0
    print(res)

def part2():
    res = 0
    with open(path.join(path.dirname(__file__), "a2.txt")) as f:
        for line in f:
            x = list(map(int, line.split()))
            for i in range(len(x)):
                s = x[:i] + x[i+1:]
                increasing = s[0] < s[-1]
                safe = True
                for prev, curr in zip(s, s[1:]):
                    safe &= is_safe(prev, curr, increasing)
                if safe:
                    res += 1
                    break
    print(res)

part1()
part2()
