#Day 2 puzzle
import copy 

data = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,1,9,19,23,2,13,23,27,2,27,13,31,2,31,10,35,1,6,35,39,1,5,39,43,1,10,43,47,1,5,47,51,1,13,51,55,2,55,9,59,1,6,59,63,1,13,63,67,1,6,67,71,1,71,10,75,2,13,75,79,1,5,79,83,2,83,6,87,1,6,87,91,1,91,13,95,1,95,13,99,2,99,13,103,1,103,5,107,2,107,10,111,1,5,111,115,1,2,115,119,1,119,6,0,99,2,0,14,0]

def opCode(noun, verb, data):
    #shallow copy of original input to avoid mutation.
    input_data = copy.copy(data)
    
    input_data[1] = noun
    input_data[2] = verb
   
   #loop through input data by jumping 4 positions on every iteration
    i = 0
    while i < len(input_data):

        #halt the program
        if input_data[i] == 99: 
            return input_data[0]
       
       #we add values found on next two positions
        if input_data[i] == 1:
            num_1 = input_data[input_data[i + 1]]
            num_2 = input_data[input_data[i + 2]]
           
           #replace the result value on third position index value
            input_data[input_data[i + 3]] = num_1 + num_2

        #we multiply values found on next two positions   
        if input_data[i] == 2:
            num_1 = input_data[input_data[i + 1]]
            num_2 = input_data[input_data[i + 2]]
           
            input_data[input_data[i + 3]] = num_1 * num_2


        i += 4

#Brute force nouns and verbs to check if we get the desired results   
def findNounVerb():
    for i in range(0, 100):
        for j in range(0, 100):
            if opCode(i, j, data) == 19690720: 
                return (100 * i + j)
                    
                
        

print(opCode(12, 2, data))
print(findNounVerb())

