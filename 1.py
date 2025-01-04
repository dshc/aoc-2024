from os import path

a = []
b = []

with open(path.join(path.dirname(__file__), "a1.txt")) as f:
    for line in f:
        x, y = line.split()
        a.append(int(x))
        b.append(int(y))

a.sort()
b.sort()

# Part 1
print(sum([abs(x[0] - x[1]) for x in zip(a, b)]))

s = {x:0 for x in a}
for x in b:
    if x in s:
        s[x] += 1

# Part 2
print(sum([x * y for x, y in s.items()]))
