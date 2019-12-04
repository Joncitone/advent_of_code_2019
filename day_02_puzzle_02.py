intcode_list = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,1,13,23,27,1,6,27,31,1,31,10,35,1,35,6,39,1,39,13,43,2,10,43,47,1,47,6,51,2,6,51,55,1,5,55,59,2,13,59,63,2,63,9,67,1,5,67,71,2,13,71,75,1,75,5,79,1,10,79,83,2,6,83,87,2,13,87,91,1,9,91,95,1,9,95,99,2,99,9,103,1,5,103,107,2,9,107,111,1,5,111,115,1,115,2,119,1,9,119,0,99,2,0,14,0]


#Goal is to find program that results in the output of 19690720 instead of the current output of 3706713, so I have to find the correct values (noun,verb) in positions 1,2 of the intcode_list in order to produce the 19690720 output

#Idea 1 is to run a nested loop that will start with a noun of 1, and iterate through all verbs 1-98, then a noun of 2, and iterate through all verbs 1-98, until the desired 19690720 output is reached, at which point the noun and verb will be recorded and the answer will be given by the formula 100*noun + verb


for i in range(0, len(intcode_list), 4):
    if(intcode_list[i] == 99):
        break
    if(intcode_list[i] == 1):
        op1sum= intcode_list[intcode_list[i + 1]] + intcode_list[intcode_list[i + 2]]
        intcode_list[intcode_list[i + 3]]= op1sum
    if(intcode_list[i] == 2):
        op2prd= intcode_list[intcode_list[i + 1]] * intcode_list[intcode_list[i + 2]]
        intcode_list[intcode_list[i + 3]]= op2prd

print(intcode_list)