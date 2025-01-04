from os import path
import re

r = re.compile(r"mul\((?P<a>[0-9]{1,3}),(?P<b>[0-9]{1,3})\)")
do_split_regex = re.compile(r"do\(\)")
dont_split_regex = re.compile(r"don't\(\)")

with open(path.join(path.dirname(__file__), "a3.txt")) as f:
   matches = [m.groupdict() for m in r.finditer(f.read())]
   print(sum([int(m["a"]) * int(m["b"]) for m in matches])) # part 1

with open(path.join(path.dirname(__file__), "a3.txt")) as f:
    lines = re.split(do_split_regex, f.read())
    res = 0
    for l in lines:
        dos = re.split(dont_split_regex, l)
        matches = [m.groupdict() for m in r.finditer(dos[0])]
        res += sum([int(m["a"]) * int(m["b"]) for m in matches]) # part 2
    print(res)
