import variables
import instruction_cycle

def print_registers():
    print("PC= "+ str(variables.PC))
    print("MAR= "+ str(variables.MAR))
    print("MDR= "+ str(variables.MDR))
    print("IR= "+ str(variables.IR))
    print("ACUMULATOR= "+ str(variables.ACUMULATOR))
    print("ALU= "+ str(variables.ALU))
    print("CU= "+ str(variables.CU))


def user_input_file(file_path):
    f = open(file_path, "r")

    counter = 0
    for x in f:
        if( x[len(x)-1] == '\n' ):
            x = x[:-1]
        
        data = x.split(" ")
        for i in range(1, len(data)-1):

            if( data[i][0]=='D'  and data[i]!='NULL' ):
                data[i] = int( data[i][1:] )
            elif( data[i]!='NULL' ):
                data[i] = float( data[i] )


        variables.memory[variables.instructions_starting_index + counter] = data
        counter+=1
   

    instruction_cycle.set_PC(variables.instructions_starting_index)


def user_input_console():
    counter=0

    while(True):
        data = input( )
        data = data.split(" ")

        for i in range(1, len(data)):
            
            if( data[i][0]=='D'  and data[i]!='NULL' ):
                data[i] = int( data[i][1:] )
                
            elif( data[i]!='NULL' ):
                data[i] = float( data[i] )


        variables.memory[variables.instructions_starting_index + counter] = data
        counter+=1

        if(data[0] == "END"):
            break
        # elif(data[0] == "PRINT"):
        #     print_registers()


    instruction_cycle.set_PC(variables.instructions_starting_index)

       

def get_processor_instructions_starting_index():
    flag = True    
    index = variables.instructions_starting_index
    
    while(flag):
        if(variables.memory[index][0]=="SET"):
            index+=1
        else:
            flag = False
            return index

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

    if memory_address in variables.memory:
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