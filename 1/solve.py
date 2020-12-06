from itertools import combinations 

#An array of all the numbers from the input file stripped 
permuteArray = []

#Just basic text processing stuff
with open("input.txt") as f:
    for line in f:

        #Turn the value into an int and strip the newline from the end
        permuteArray.append(int(line[:-1]))

#Use a combination because we don't want repeats of the same tuples
comb = combinations(permuteArray,2)

#Loop through the tuples and check 
#1) if they sum to 2020
#2) what their product is
for value in comb:
    if (value[0]+value[1] == 2020):
        print(value[0]*value[1])
        exit
