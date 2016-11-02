import random

def randConst():
    return "#" + str(random.randrange(0,7))

def randOffset():
    return "#" + str(random.randrange(0,32)*4)

def randRegister():
    return "R" + str(random.randrange(0,8))

def register():
    return bool(random.randrange(0,2))


none = 0
two = 1
index = 2
three = 3
instr =     ["ADDS", "SUBS", "LDR", "LDR", "LDR", "LDR", "STR", "STR", "STR", "STR", "ANDS", "EORS", "ORRS", "MVNS", "NOP"]
operands =  [ three,  three, index, index, index, index, index, index, index, index,  two,    two,    two,    two,    none]


total_instructions = 100

print("")
print("NOP")
for _ in range(0,total_instructions):
    rand = random.randrange(0, len(instr))
    current_instruction = instr[rand]
    current_operands = operands[rand]
    if current_operands == none:
        print(current_instruction)
    if current_operands == two:
        print(current_instruction + " " + randRegister() + ", " + randRegister())
    if current_operands == index:
        print(current_instruction + " " + randRegister() + ", [" + randRegister() + ", " + randOffset() + "]")
    if current_operands == three:
        print(current_instruction + " " + randRegister() + ", " + randRegister() + ", " + (randRegister() if register() else randConst()))

print("NOP")
print("NOP")
print("NOP")
print("NOP")
print("HALT")
