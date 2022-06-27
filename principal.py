
PC = None ##Program counter
IR = None ##Instruction register
MAR= None ##Memory address registrers 
MDR= None ##Memory data register, aka MBR(memory buffer register)
ACUMULATOR = None
ALU = None ##Unidad Aritmetico Logica
CU = None ##Control Unit 

END_flag = False

memory={}
instructions=[]

def print_registers():
    print("PC= "+ str(PC))
    print("MAR= "+ str(MAR))
    print("MDR= "+ str(MDR))
    print("IR= "+ str(IR))
    print("ACUMULATOR= "+ str(ACUMULATOR))
    print("ALU= "+ str(ALU))
    print("CU= "+ str(CU))

def user_input_file(file_path):
    f = open(file_path, "r")
    for x in f:
        data = x.split(" ")
        instructions.append(data)

        if(data[0] == "SET"):
            memory[data[1]] = int(data[2])
    
    memory_index_firts_instruction = move_instructions_to_memory(100)
    set_PC(memory_index_firts_instruction)


def move_instructions_to_memory(initial_memomry_addres):

    aux= get_processor_instructions_starting_index()
    num_processor_instructions =  abs(aux - len(instructions))
    
    temp= initial_memomry_addres
    while(True):

        flag= check_range_of_avalible_memory("D"+str(temp), "D"+str(num_processor_instructions + temp))
    
        if(not flag):
            temp += num_processor_instructions+10 
        else:
            break


    for i in range(aux, len(instructions)):
        memory["D"+str(temp + i - aux )] = instructions[i]
        
    return temp


def get_processor_instructions_starting_index():
    counter=0
    for i in instructions:
        if(i[0]=="SET"):
            counter+=1
        else:
            return counter

def get_amount_of_non_NULL_elements(list):
    counter=0
    for i in list:
        if(i=="NULL"):
            break
        else:
            counter+=1
    
    return counter

def check_for_avalible_memory(memory_address):
    flag=True

    if memory_address in memory:
        flag=False
    
    return flag

def check_range_of_avalible_memory(initial_address, last_address):

    initial_address = int (initial_address[1:])
    last_address = int (last_address[1:])

    flag= True
    for i in range(initial_address, last_address+1):
        flag = check_for_avalible_memory("D"+ str(i))

        if(not flag):
            break
    
    return flag


def set_PC(value):
    global PC
    PC = value


def first_step():
    global PC, MAR, MDR, IR 

    MAR = "D"+str(PC)
    MDR = memory[MAR]
    IR = MDR
    PC+=1

def second_step():
    global IR, CU
    CU = IR
    control_unit_logic(IR)

def start_processor_execution():

    while(not END_flag):
        first_step()
        second_step()



def control_unit_logic(commands):
    global END_flag

    if(commands[0]=="END"):
        END_flag = True
    elif(commands[0]=="LDR"):
        LOAD(commands)
    elif(commands[0]=="STR"):
        STORE(commands)
    elif(commands[0]=="ADD"):
        ADD(commands)
    elif(commands[0]=="SUB"):
        SUBTRACTION(commands)
    elif(commands[0]=="SHW"):
        SHOW(commands)
        

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

    counter= get_amount_of_non_NULL_elements(list)
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

    counter= get_amount_of_non_NULL_elements(list)
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




#################################

user_input_file("instrucciones.txt")

##print(instructions)
##print(memory)

start_processor_execution()
##print_registers()
##print(memory)


