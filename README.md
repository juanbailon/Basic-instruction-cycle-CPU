# Basic-instruction-cycle-CPU

This python program tries to emulate the basic instruction cycle of a CPU.

There are to ways to run the program:
>The first one is to pass a .txt file with the insstructions/commands to be executed to the function _user_input_file()_, and then call the function _start_processor_execution()_.

>The second way is  to call _user_input_console()_ and write all the insstructions/commands line by line in the terminal and then call the function _start_processor_execution()_.



## commands

The commands to interact with the program are the following:

 - **SET** - MEM - _SET D1 X_, Store X value in in D1 memory address. where X is an immediate, direct or constant value. When SET instruction is read the X value is stored in Memory without processor execution.

 * **ADD** - ADDITION - There are three ways: _ADD D1_, adds the value in D1 memory address to loaded value in accumulator
   register. _ADD D1 D3_ Load the value in D1 memory address in the
   acumulator register and adds to found value in D3 memory address.
   _ADD D1 D3 D4_ same that _ADD D1 D3_ but puts the result in D4
   
  *  **SUB** - SUBTRACTION - There are three ways: _SUB D1_, _SUB D1 D2_ and _SUB D3 D2 D1_ smiliar to ADD but perform subtraction.
   
 *  **MUL** - MULTIPLICATION - Using ADD perform multiplication operation. There are three ways: _MUL D1_, _MUL D1 D2_, _MUL D1 D2 D3_ similar to _ADD_ and _SUB_. _Multiplication
   cannot be used with an immediate/direct/constant value._
   
  * **DIV** - INTEGER DIVISION - Using SUB perform division  operation. There are three ways: DIV D1, DIV D1 D2, DIV D1 D2 D3 similar to MUL
   
  * **INC** - INCREMENT - _INC D3_ Load the value in D3 memory address adds 1 and store in same address
   
  * **DEC** - DECREMENT - _DEC D3_ Load the value in D3 memory address adds 1 and store in same address
   
  * **MOV** - MOVE - _MOV D2 D10_ Load the value in D2 memory address to D10 memory address and clear D2 address
   
  * **LDR** - LOAD - _LDR D3_ Load the value in D3 memory address and puts in acumulator register
   
  * **STR** - STORE - _STR D3_ Read the value in acumulator register and puts in D3 memory address
   
  * **BEQ** - EQUAL - _BEQ D10_ Load the value in D10 memory address if substration with acumulator register values is zero puts
   in D10 memory address. There are three ways: _BEQ D10_,
   _BEQ D1 D10_, _BEQ D1 D2 D3_
   
  * **AND** - AND GATE
   
  * **OR** - OR GATE
   
  * **SHW** - SHOW - _SHW D2 NULL NULL_ show the value in D2 memory address, _SHW ACC_ show the value in acumulator register, _SHW ICR_
   show the value in ICR register, _SHW MAR_ show the value in MAR
   register, _SHW MDR_ show the value in MDR register, _SHW UC_ show the
   value in Control Unit.
   
   * **END** - FINISH READING INSTRUCTION
    
<br>

# *Examples*

## examples of the .txt file
```sh
    SET D1 2
    SET D3 5
    LDR D2
    ADD D3
    STR D1
    SHW D1
    END
```
```sh
    SET D5 12 NULL NULL
    SET D2 23 NULL NULL
    SET D8 3 NULL NULL
    SET D3 5 NULL NULL
    LDR D2 NULL NULL NULL
    ADD D5 NULL NULL NULL
    ADD D8 NULL NULL NULL
    STR D3 NULL NULL NULL
    LDR D3 NULL NULL NULL
    ADD D2 NULL NULL NULL
    STR D2 NULL NULL NULL
    SHW D2 NULL NULL NULL
    END NULL NULL NULL
```
<br>

## Run program with commands in txt file 
For this one lest prentent that the txt file that we use is the second one given in the .txt examples before.
```sh
    user_input_file("file_path")
    start_processor_execution()
```
>output

        61

<br>

## Run program with commands given through the terminal
```sh
    user_input_console()
    start_processor_execution()
```
>Terminal
```sh
    $python3 principal.py
     SET D1 2
     SET D3 5
     LDR D2
     ADD D3
     STR D1
     SHW D1
     END
    
```

>output

        8
