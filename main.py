import utilities
import variables
import instruction_cycle
import sys


if( len(sys.argv) > 1 ): ##executed if the user gives a .txt file as a parameter through the terminal
    utilities.user_input_file( sys.argv[1] )
else:
    utilities.user_input_console()


instruction_cycle.start_processor_execution()


#print( variables.memory)
#utilities.print_registers()
