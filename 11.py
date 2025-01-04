from functools import cache
from os import path

with open(path.join(path.dirname(__file__), "a11.txt")) as f:
    numbers = [int(x) for x in f.read().split()]

@cache
def exec(starting_number, blinks_left):
    if blinks_left == 0:
        return 1
    
    if starting_number == 0:
        return exec(1, blinks_left - 1)
    
    s = str(starting_number)
    if len(s) % 2 == 0:
        mid = int(len(s) / 2)
        return exec(int(s[0:mid]), blinks_left - 1) + exec(int(s[mid:]), blinks_left - 1)
    
    return exec(starting_number * 2024, blinks_left - 1)


count = 0
for number in numbers:
    count += exec(number, 25)
print(count)

count = 0
for number in numbers:
    count += exec(number, 75)
print(count)