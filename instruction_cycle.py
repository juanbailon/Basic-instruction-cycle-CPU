from variables import PC, IR, MAR, MDR, CU, memory, END_flag
import commands


def set_PC(value):
    global PC
    PC = value


## the first step to do in the instrucion cycle
def first_step():
    global PC, MAR, MDR, IR 

    MAR = PC
    MDR = memory[MAR]
    IR = MDR
    PC+=1

## the second step to do in the instrucion cycle
def second_step():
    global IR, CU
    CU = IR
    control_unit_logic(IR)

def start_processor_execution():

    while(not END_flag):
        first_step()
        second_step()



def control_unit_logic(instructions):
    global END_flag

    if(instructions[0]=="END"):
        END_flag = True
    elif(instructions[0]=="SET"):
        commands.SET(instructions)
    elif(instructions[0]=="LDR"):
        commands.LOAD(instructions)
    elif(instructions[0]=="STR"):
        commands.STORE(instructions)
    elif(instructions[0]=="ADD"):
        commands.ADD(instructions)
    elif(instructions[0]=="SUB"):
        commands.SUBTRACTION(instructions)
    elif(instructions[0]=="MUL"):
        commands.MULTIPLICATION(instructions)
    elif(instructions[0]=="DIV"):
        commands.INTEGER_DIVISON(instructions)
    elif(instructions[0]=="INC"):
        commands.INCREMENT(instructions)
    elif(instructions[0]=="DEC"):
        commands.DECREMENT(instructions)
    elif(instructions[0]=="MOV"):
        commands.MOVE(instructions)
    elif(instructions[0]=="AND"):
        commands.AND_GATE(instructions)
    elif(instructions[0]=="OR"):
        commands.OR_GATE(instructions)
    elif(instructions[0]=="BEQ"):
        commands.EQUAL(instructions)
    elif(instructions[0]=="SHW"):
        commands.SHOW(instructions)
  