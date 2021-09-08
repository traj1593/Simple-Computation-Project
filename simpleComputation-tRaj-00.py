'''
Program: Simple Computation
Filename: simpleComputation-tRaj-00.py
Author: Tushar Raj
Description: The program accepts diameter of circle as a user input and prints the circumference of the circle.
Revisions: No revisions made
'''
### Step 1: Announce, prompt and get response

#Announce
print("****Simple Computation : circumference of the circle****\n")
#Prompt user to get response
number = input("Please enter the diameter of the circle: ")


### Step 2: Convert the diameter to float data and see that the input vlaue is non negative value and also not a string

#check if the user input is negative or string, if it is then print the error message and ask to enter the input again.
count = 1
while(count):
    if((number.isalpha()==True)): #checks if the value entered in number is having any character or not
        print("****diameter of the circle cant be a string****\n") #prints the error message
        progress = input("Please enter if you waant to continue with calculation of circumference of the circle(y/n): ") #ask users if he wants to continue with program
        if( progress == 'y' or progress == 'Y' ):#checks the response of the user if its y, he asks to enter the diameter again
            number = input("Please enter the diameter of the circle: ")
        if( progress == 'n' or progress == 'N' ):#exits the program if response in n
            exit()
        continue
    elif(float(number) < 0): # checks if the entered user input is negative
        print("****diameter of the circle cant be a negative value****\n")
        progress = input("Please enter if you waant to continue with calculation of circumference of the circle(y/n): ")
        if( progress == 'y' or progress == 'Y' ):
            number = input("Please enter the diameter of the circle: ")
        if( progress == 'n' or progress == 'N' ):
            exit()
        continue
	#if it is not a negative number or string then convert the value from string to float data type and come out of the loop
    else:
        diameter = float(number)
        break;
    
### Step 3: Compute the circumference of the circle

# This calculates the circumference of circle(2πr), where 2 times r is the diamter of circle and value of π is multiplied
#Another way to calculate this is by importing math libraby and using math.pi instead of 3.14159
circumference = diameter * 3.14159 

#print the result
print("The circumference of a circle of diameter {0} is {1}".format(diameter,circumference),".")
print("\n****End of circumference of the circle program****")