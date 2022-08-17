from variables import IR, MAR, MDR, ACUMULATOR, ALU, CU, memory
import utilities

def SET(list):
    memory[ list[1] ] = list[2]

def LOAD(list):
    global MAR, MDR, ACUMULATOR

    MAR = list[1]
    MDR = memory[MAR]
    ACUMULATOR = MDR

def STORE(list):
    global MAR, MDR

    MAR = list[1]
    MDR = ACUMULATOR
    memory[MAR] = MDR


def ADD(list):
    global ALU, ACUMULATOR, MAR, MDR

    counter= utilities.get_amount_of_non_NULL_elements(list)
    counter-=1
    
    if(counter==1):
        ALU = ACUMULATOR
        MAR = list[1]
        MDR = memory[MAR]
        ACUMULATOR = MDR
        
        ALU += ACUMULATOR
        ACUMULATOR = ALU
    
    elif(counter==2):
        LOAD(["LDR", list[1] ])
        ADD(["ADD", list[2] ])
    
    elif(counter==3):
        ADD(["ADD", list[1], list[2] ])
        STORE(["STR", list[3] ])


def SUBTRACTION(list):
    global ALU, ACUMULATOR, MAR, MDR

    counter= utilities.get_amount_of_non_NULL_elements(list)
    counter-=1

    if(counter==1):
        ALU = ACUMULATOR
        MAR = list[1]
        MDR = memory[MAR]
        ACUMULATOR = MDR

        ALU -= ACUMULATOR
        ACUMULATOR = ALU
    
    elif(counter==2):
        LOAD(["LDR", list[1] ])
        SUBTRACTION(["SUB", list[2] ])

    elif(counter==3):
        SUBTRACTION(["SUB", list[1], list[2] ])
        STORE(["STR", list[3] ])


def MULTIPLICATION(list):
    global ACUMULATOR, MAR, MDR

    counter= utilities.get_amount_of_non_NULL_elements(list)
    counter-=1

    if(counter==1):        
        MAR = list[1]
        MDR = memory[MAR]
        
        ACUMULATOR = int(ACUMULATOR)
        for i in range(ACUMULATOR-1):
            if(i==0):
                LOAD(["LDR", MAR])
            ADD(["ADD", MAR])
        
    elif(counter==2):
        LOAD(["LDR", list[1] ])
        MULTIPLICATION(["MUL", list[2] ])
    
    elif(counter==3):
        MULTIPLICATION(["MUL", list[1], list[2] ])
        STORE(["STR", list[3] ])
            

def INTEGER_DIVISON(list):
    global ACUMULATOR, MAR, MDR

    counter= utilities.get_amount_of_non_NULL_elements(list)
    counter-=1
    
    if(counter==1):
        MAR = list[1]
        MDR = memory[MAR]

        temp=0
        while(True):
            SUBTRACTION(["SUB", MAR])

            if(ACUMULATOR>=0):
                temp+=1
            if(ACUMULATOR<=0):
                ACUMULATOR = temp
                break
    
    elif(counter==2):
        LOAD(["LDR", list[1] ])
        INTEGER_DIVISON(["DIV", list[2] ])

    elif(counter==3):
        INTEGER_DIVISON(["DIV", list[1], list[2] ])
        STORE(["STR", list[3] ])


def INCREMENT(list):
    global ALU, ACUMULATOR

    LOAD(["LDR", list[1] ])
    ALU = ACUMULATOR
    ALU = ALU+1
    ACUMULATOR = ALU
    STORE(["STR", list[1] ])


def DECREMENT(list):
    global ALU, ACUMULATOR

    LOAD(["LDR", list[1] ])
    ALU = ACUMULATOR
    ALU = ALU-1
    ACUMULATOR = ALU
    STORE(["STR", list[1] ])


def MOVE(list):
    global MDR

    LOAD(["LDR", list[1] ])
    MDR = 0
    memory[MAR] = MDR
    STORE(["STR", list[2] ])


def EQUAL(list):

    counter= utilities.get_amount_of_non_NULL_elements(list)
    counter-=1

    if(counter==1):
        SUBTRACTION(["SUB", list[1]] )
        if(ACUMULATOR==0):
            ACUMULATOR=True
            STORE(["STR", list[1] ])
        else:
            ACUMULATOR=False
            STORE(["STR", list[1] ])
    
    elif(counter==2):
        SUBTRACTION(["SUB", list[1], list[2] ])
        if(ACUMULATOR==0):
            ACUMULATOR=True
            STORE(["STR", list[2] ])
        else:
            ACUMULATOR=False
            STORE(["STR", list[2] ])
    
    elif(counter==3):
        SUBTRACTION(["SUB", list[1], list[2] ])
        if(ACUMULATOR==0):
            ACUMULATOR=True
            STORE(["STR", list[3] ])
        else:
            ACUMULATOR=False
            STORE(["STR", list[3] ])

    

def AND_GATE(list):
    global ACUMULATOR, MAR, MDR, ALU

    counter= utilities.get_amount_of_non_NULL_elements(list)
    counter-=1

    if(counter==1):
        ALU = ACUMULATOR
        MAR = list[1]
        MDR = memory[MAR]
        ACUMULATOR = MDR

        ALU = ALU and ACUMULATOR
        ACUMULATOR = ALU

    elif(counter==2):
        LOAD(["LDR", list[1] ])
        AND_GATE(["AND", list[2] ])

    elif(counter==3):
        AND_GATE(["AND", list[1], list[2] ])
        STORE(["STR", list[3] ])


def OR_GATE(list):
    global ACUMULATOR, MAR, MDR, ALU

    counter= utilities.get_amount_of_non_NULL_elements(list)
    counter-=1

    if(counter==1):
        ALU = ACUMULATOR
        MAR = list[1]
        MDR = memory[MAR]
        ACUMULATOR = MDR

        ALU = ALU or ACUMULATOR
        ACUMULATOR = ALU
    
    elif(counter==2):
        LOAD(["LDR", list[1] ])
        OR_GATE(["OR", list[2] ])

    elif(counter==3):
        OR_GATE(["OR", list[1], list[2] ])
        STORE(["STR", list[3] ])


def SHOW(list):

    if(list[1]=="ACC"):
        print(ACUMULATOR)
    elif(list[1]=="ICR"):
        print(IR)
    elif(list[1]=="MAR"):
        print(MAR)
    elif(list[1]=="MDR"):
        print(MDR)
    elif(list=="UC"):
        print(CU)
    else:
        print( memory[list[1]] )
