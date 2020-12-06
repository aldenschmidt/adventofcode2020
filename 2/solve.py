#Checks if the occurances of letter in password are within defined bounds.
def validate(lowerBound, upperBound, letter, password):
    letterCount = password.count(letter)
    return True if letterCount >= lowerBound and letterCount <= upperBound else False

validPasswords = 0 #This is our counter for the total number of valid passwords

with open("input.txt") as f:
    for line in f: 
        
        line = line.replace("-"," ") #Get rid of the dash
        line = line.replace(":","")  #Get rid of the colon
        line = line.split(" ")       #Split on the spaces

        #Call the validate function on each part of the string 
        if validate(int(line[0]), int(line[1]), line[2], line[3][:-1]) == True:
        	validPasswords += 1 

print(validPasswords) #Result