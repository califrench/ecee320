import random, string

def randConst():
    return "#" + str(random.randrange(0,7))

def randOffset():
    return "#" + str(random.randrange(0,32)*4)

def randRegister():
    return "R" + str(random.randrange(0,8))

def register():
    return bool(random.randrange(0,2))

def randLabel():
   return ''.join(random.choice(string.ascii_uppercase) for i in range(5))


none = 0
two = 1
index = 2
three = 3
branch = 4
label = 5
instr =     ["ADDS", "SUBS", "ADDS", "SUBS", "ADDS", "SUBS", "LDR", "LDR", "LDR", "LDR", "STR", "STR", "STR", "STR", "ANDS", "EORS", "ORRS", "MVNS", "ANDS", "EORS", "ORRS", "MVNS", "NOP", "BEQ", "BNE", "BCS", "BCC", "BMI", "BPL", "BVS", "BVC", "LABEL"]
operands =  [ three,  three, three,  three, three,  three, index, index, index, index, index, index, index, index,  two,    two,    two,    two,  two,    two,    two,    two,  none, branch,branch,branch,branch,branch,branch,branch,branch,label]



total_instructions = 30

print("")
print("NOP")

labels = []

branchesLeft = 4

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
    if current_operands == label:
        if len(labels) > 4:
            newLabel = randLabel()
            labels.append(newLabel)
            print(newLabel + ":")
    if current_operands == branch:
        if branchesLeft > 0:
            branchesLeft -= 1
            if len(labels) > 0:
                curLabel = random.choice(labels)
                print(current_instruction + " " + curLabel)
            else:
                newLabel = randLabel()
                labels.append(newLabel)
                print(newLabel + ":")

print("NOP")
print("NOP")
print("NOP")
print("NOP")
print("HALT")
