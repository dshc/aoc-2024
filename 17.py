from math import floor
from os import path

def read():
    registers = []
    with open(path.join(path.dirname(__file__), "a17.txt")) as f:
        for line in f:
            if "Register" in line:
                registers.append(int(line.strip().split(":")[1].strip()))
            elif "Program" in line:
                p = line.strip().split(":")[1]
                program = [int(x.strip()) for x in p.split(",")]
    return registers, program

def get_combo_value(operand, registers):
    if operand >= 0 and operand <= 3:
        return operand
    return registers[operand % 4]

def adv(iptr, operand, r):
    numerator = r[0]
    denominator = 2**get_combo_value(operand, r)
    return (iptr + 2, [floor(numerator/denominator), r[1], r[2]])
    
def bxl(iptr, operand, r):
    return (iptr + 2, [r[0], r[1] ^ operand, r[2]])

def bst(iptr, operand, r):
    return (iptr + 2, [r[0], get_combo_value(operand, r) % 8, r[2]])

def jnz(iptr, operand, r):
    if r[0] == 0:
        return (iptr + 2, r)
    
    new_iptr = operand
    if new_iptr == iptr:
        return (iptr + 2, r)
    else:
        return (new_iptr, r)

def bxc(iptr, operand, r):
    return (iptr + 2, [r[0], r[1]^r[2], r[2]])

def out(iptr, operand, r, outputs):
    outval = get_combo_value(operand, r) % 8
    outputs.append(outval)
    return (iptr + 2, r)

def bdv(iptr, operand, r):
    numerator = r[0]
    denominator = 2**get_combo_value(operand, r)
    return (iptr + 2, [r[0], floor(numerator/denominator), r[2]])

def cdv(iptr, operand, r):
    numerator = r[0]
    denominator = 2**get_combo_value(operand, r)
    return (iptr + 2, [r[0], r[1], floor(numerator/denominator)])

registers, program = read()

outputs = []
iptr = 0
while iptr < len(program) - 1:
    match program[iptr]:
        case 0:
            next_iptr, next_reg = adv(iptr, program[iptr+1], registers)
        case 1:
            next_iptr, next_reg = bxl(iptr, program[iptr+1], registers)
        case 2:
            next_iptr, next_reg = bst(iptr, program[iptr+1], registers)
        case 3:
            next_iptr, next_reg = jnz(iptr, program[iptr+1], registers)
        case 4:
            next_iptr, next_reg = bxc(iptr, program[iptr+1], registers)
        case 5:
            next_iptr, next_reg = out(iptr, program[iptr+1], registers, outputs)
        case 6:
            next_iptr, next_reg = bdv(iptr, program[iptr+1], registers)
        case 7:
            next_iptr, next_reg = cdv(iptr, program[iptr+1], registers)
    iptr = next_iptr
    registers = next_reg
        
print(','.join(map(str, outputs)))