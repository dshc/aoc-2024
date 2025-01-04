from os import path
from collections import defaultdict
from math import floor
from functools import cmp_to_key

rules = defaultdict(list)
updates = []
with open(path.join(path.dirname(__file__), "a5.txt")) as f:
    for line in f:
        if line.strip() == "":
            continue
        elif '|' in line:
            s = list(map(int, line.strip().split('|')))
            rules[s[0]].append(s[1])
        else:
            s = list(map(int, line.strip().split(',')))
            updates.append(s)

middles = []

def valid(u):
    seen = set()
    for x in u:
        for y in seen:
            if y in rules[x]:
                return False
        seen.add(x)
    return True

for update in updates:
    if valid(update):
        middles.append(update[floor(len(update)/2)])
print(sum(middles)) # part 1

def compare(l, r):
    if r in rules[l]:
        return -1
    if l in rules[r]:
        return 1
    return 0

middles_2 = []
for update in updates:
    if not valid(update):
        update = sorted(update, key=cmp_to_key(compare))
        middles_2.append(update[floor(len(update)/2)])
print(sum(middles_2)) # part 2