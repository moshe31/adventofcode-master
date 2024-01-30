# Day 5
import copy

program = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,40,93,224,1001,224,-3720,224,4,224,102,8,223,223,101,3,224,224,1,224,223,223,1101,56,23,225,1102,64,78,225,1102,14,11,225,1101,84,27,225,1101,7,82,224,1001,224,-89,224,4,224,1002,223,8,223,1001,224,1,224,1,224,223,223,1,35,47,224,1001,224,-140,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1101,75,90,225,101,9,122,224,101,-72,224,224,4,224,1002,223,8,223,101,6,224,224,1,224,223,223,1102,36,63,225,1002,192,29,224,1001,224,-1218,224,4,224,1002,223,8,223,1001,224,7,224,1,223,224,223,102,31,218,224,101,-2046,224,224,4,224,102,8,223,223,101,4,224,224,1,224,223,223,1001,43,38,224,101,-52,224,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,1102,33,42,225,2,95,40,224,101,-5850,224,224,4,224,1002,223,8,223,1001,224,7,224,1,224,223,223,1102,37,66,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1007,226,677,224,1002,223,2,223,1005,224,329,1001,223,1,223,1007,226,226,224,1002,223,2,223,1006,224,344,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,359,1001,223,1,223,108,677,677,224,1002,223,2,223,1006,224,374,1001,223,1,223,107,677,677,224,1002,223,2,223,1005,224,389,101,1,223,223,8,677,677,224,1002,223,2,223,1005,224,404,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,419,101,1,223,223,1008,677,677,224,1002,223,2,223,1005,224,434,101,1,223,223,1008,226,226,224,1002,223,2,223,1005,224,449,101,1,223,223,7,677,226,224,1002,223,2,223,1006,224,464,1001,223,1,223,7,226,226,224,1002,223,2,223,1005,224,479,1001,223,1,223,1007,677,677,224,102,2,223,223,1005,224,494,101,1,223,223,1108,677,226,224,102,2,223,223,1006,224,509,1001,223,1,223,8,677,226,224,102,2,223,223,1005,224,524,1001,223,1,223,1107,226,226,224,102,2,223,223,1006,224,539,1001,223,1,223,1008,226,677,224,1002,223,2,223,1006,224,554,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,569,1001,223,1,223,1108,677,677,224,102,2,223,223,1005,224,584,101,1,223,223,7,226,677,224,102,2,223,223,1006,224,599,1001,223,1,223,1108,226,677,224,102,2,223,223,1006,224,614,101,1,223,223,107,226,677,224,1002,223,2,223,1005,224,629,101,1,223,223,108,226,677,224,1002,223,2,223,1005,224,644,101,1,223,223,8,226,677,224,1002,223,2,223,1005,224,659,1001,223,1,223,107,226,226,224,1002,223,2,223,1006,224,674,101,1,223,223,4,223,99,226]

def opCode(input_instruction, program):
    input_data = copy.copy(program)
    start = True
    i = 0
    while (start):
        input = input_data[i: i + 4]
        modes = str(input[0])
        modes_length = len(modes)
        opCode = input[0] % 100

        #concat 0's if mode length is less then 5
        if modes_length < 5:
            for r in range(0, 5 - modes_length):
                modes = ''.join(('0', modes))

        #find the parameter on current position
        def getParams(position):
            positionMode = modes[3 - position] == '0'
            if positionMode:
                return input_data[input[position]]
            else:
        #return current position value        
                return input[position]

        #Opcode 1 and 2 are works exactly the same as day 2 puzzle 
        if opCode == 1:
            input_data[input[3]] = getParams(1) + getParams(2)
            i += 4

        if opCode == 2:
            input_data[input[3]] = getParams(1) * getParams(2)
            i += 4

        # Opcode 3 takes a single integer as input and saves it to the position given by its only parameter.
        if opCode == 3:
            input_data[input[1]] = input_instruction.pop()
            i += 2

        # Opcode 4 outputs the value of its only parameter.
        if opCode == 4:
            result = getParams(1)
            i += 2

            if result:
                start = False
                return result
        
        # Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. 
        # Otherwise, it does nothing.
        if opCode == 5:
            if getParams(1) != 0:
                i = getParams(2)
            else:
                i += 3

        # Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter.
        # Otherwise, it does nothing.
        if opCode == 6:
            if getParams(1) == 0:
                i = getParams(2)
            else:
                i += 3

        # Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter.
        # Otherwise, it stores 0.
        if opCode == 7:
            if getParams(1) < getParams(2):
                input_data[input[3]] = 1
            else:
                input_data[input[3]] = 0

            i += 4

        # Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter.
        # Otherwise, it stores 0.
        if opCode == 8:
            if getParams(1) == getParams(2):
                input_data[input[3]] = 1
            else:
                input_data[input[3]] = 0

            i += 4

        #halt the program
        if opCode == 99:
            start = False

#puzzle 1
print(opCode([1], program))

#puzzle 1
print(opCode([5], program))
