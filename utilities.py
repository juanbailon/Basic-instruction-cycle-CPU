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


## read the instructions from a .txt file
def user_input_file(file_path):
    f = open(file_path, "r")

    counter = 0
    for x in f:
        if( x[len(x)-1] == '\n' ):
            x = x[:-1]
        
        data = x.split(" ")
        for i in range(1, len(data)):

            if( data[i][0]=='D'  and data[i]!='NULL' ):
                data[i] = int( data[i][1:] )
            elif( data[i]!='NULL' ):
                data[i] = float( data[i] )


        variables.memory[variables.instructions_starting_index + counter] = data
        counter+=1
   

    instruction_cycle.set_PC(variables.instructions_starting_index)


## reads the instructions from the console
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

    instruction_cycle.set_PC(variables.instructions_starting_index)



def get_amount_of_non_NULL_elements(list):
    counter=0
    for i in list:
        if(i=="NULL"):
            break
        else:
            counter+=1
    
    return counter
