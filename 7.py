from os import path

def exec(test_value, curr, variables):
    if not variables: return curr == test_value
    return exec(test_value, curr*variables[0], variables[1:]) or exec(test_value, curr+variables[0], variables[1:])

def exec2(test_value, curr, variables):
    if not variables: return curr == test_value
    return exec2(test_value, curr*variables[0], variables[1:]) or\
           exec2(test_value, curr+variables[0], variables[1:]) or\
           exec2(test_value, int(str(curr) + str(variables[0])), variables[1:])

result = 0
result2 = 0
with open(path.join(path.dirname(__file__), "a7.txt")) as f:
    for line in f:
        equation = [x.strip() for x in line.split(':')]
        test_value = int(equation[0])
        variables = [int(x) for x in equation[1].split()]
        if exec(test_value, variables[0], variables[1:]):
            result += test_value
        if exec2(test_value, variables[0], variables[1:]):
            result2 += test_value

print(result) # part 1
print(result2) # part 2