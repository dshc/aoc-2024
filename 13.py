from functools import cache
from os import path

def parse():
    def parse_button(s):
        tmp =  [int(y.split('+')[1]) for y in [x.strip() for x in s.split(',')]]
        return (tmp[0], tmp[1])

    def parse_prize(s):
        tmp =  [int(y.split('=')[1]) for y in [x.strip() for x in s.split(',')]]
        return (tmp[0], tmp[1])

    games = [{}]
    with open(path.join(path.dirname(__file__), "a13.txt")) as f:
        for line in f:
            s = [x.strip() for x in line.split(':')]
            if len(s) == 1:
                games.append({})
                continue

            if s[0] == "Button A":
                games[-1]["a"] = parse_button(s[1]) 
            elif s[0] == "Button B":
                games[-1]["b"] = parse_button(s[1]) 
            else:
                games[-1]["prize"] = parse_prize(s[1])

    return games


def score(counts):
    return counts[0]*3 + counts[1] if counts != None else 0

def exec(game):
    a = game["a"]
    b = game["b"]

    @cache
    def search(count_a, count_b, prize_x, prize_y):
        if prize_x == prize_y == 0:
            return (count_a, count_b)

        if prize_x < 0 or prize_y < 0:
            return None

        if count_a > 100 or count_b > 100:
            return None

        press_a = search(count_a+1, count_b, prize_x - a[0], prize_y - a[1])
        press_b = search(count_a, count_b+1, prize_x - b[0], prize_y - b[1])

        if press_a == None and press_b != None:
            return press_b
        elif press_a != None and press_b == None:
            return press_a
        elif press_a != None and press_b != None:
            return press_a if score(press_a) < score(press_b) else press_b
        else:
            return None

    return search(0, 0, game["prize"][0], game["prize"][1])


cost = 0
for game in parse():
    cost += score(exec(game))
print(cost)


def exec2(game):
    a = game["a"]
    b = game["b"]
    prize = (game["prize"][0] + 10000000000000, game["prize"][1] + 10000000000000)

    ax_times_by = a[0] * b[1]
    ay_times_bx = a[1] * b[0]
    effective_a = ax_times_by - ay_times_bx

    px_times_by = prize[0] * b[1]
    py_times_bx = prize[1] * b[0]
    effective_p = px_times_by - py_times_bx

    a_presses = effective_p / effective_a
    b_presses = (prize[1] - (a_presses * a[1])) / b[1]
    if a_presses.is_integer() and b_presses.is_integer():
        return (a_presses, b_presses)
    else:
        return None

cost = 0
for game in parse():
    cost += score(exec2(game))
print(int(cost))