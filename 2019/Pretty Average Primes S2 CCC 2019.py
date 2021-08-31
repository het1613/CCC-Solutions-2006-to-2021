def prime_identifier(number): #This defines a function called "prime_identifier" which has 1 parameter, an integer in this case called number
    for divisor in range(2,number): #This creates a for loop that has an integer varaible divisor which starts at 0 and repeats the statements below unti divisor is equal to number (divisor incremented each time loop is passed automatically)
        if (number%divisor==0): #checks if the number is divisible by the divisor
            return False #if it is, the number is not prime and the function returns False
    else: #this else statment will only be reached if the for loop is completed without breaking
        return True #if the for loop passes without breaking, it means the number is prime and returns True

num_of_tests=int(input()) #Asks the user to input the number of test cases which is converted from a string and stored as an integer in the variable "num_of_tests"

all_outputs=[] #This creates an empty list which is assigned to the varaible "all_outputs". This list will hold all the outputs of the test cases and will output at the end all once al the tests are done
infinity=9999999999999999999999999999 #"infinity" varaible holds an exremenly large number which for our purposes we will consider infinity. This will be our end for our for loops

for current_test in range(num_of_tests): #This creates a for loop which repeats the statements below for num_of_tests times
    num=int(input()) #Asks the user to input an integer which will be the average of two primes. The inout is converted from a string and stored as an integer in the variable "num"
    
    for number_A in range(2,infinity): #Creates a for loop which repeats the statments for infinity. number_A which is a possible prime starts at 2 and increments by 1 forever 
        if (prime_identifier(number_A)): #checks if the output from the function "prime_identifier" is True
                                         #The function has 1 argument which is an integer, in this case we are feeding number_A to it. The outout will either be True or False which either passes the if condition or doesn't pass it

            #if the condition is True, the following statments are run
            for number_B in range(2,infinity): #Creates a for loop which repeats the statments for infinity. number_B which is a possible prime starts at 2 and increments by 1 forever
                if (prime_identifier(number_B)): #checks if the output from the function "prime_identifier" is True
                                                 #The function has 1 argument which is an integer, in this case we are feeding number_B to it. The outout will either be True or False which either passes the if condition or doesn't pass it

                    if ((number_A+number_B)/2>=num): #if the previous if condition is True, it checks if the average of number_A and number_B is greater or equal to the intial number enetered by the user
                        break #if it is, the thrid loop must be broken as if it continues, number_B will get higher and the average will get higher, and we will be in an infinite loop.

            if ((number_A+number_B)/2==num): #checks if the average of number_A and number_B is equal to num
                all_outputs.append(str(number_A)+' '+str(number_B)) #if it is, we have found our pair of numbers and they can be appended to all_outputs as a string using the .append() function
                break #pair is found so second loop can be exited/broken
            
print('\n'.join(all_outputs)) #This prints all the strings in the list "all_outputs" in new lines due to '\n' using the .join() function to the users screen
    
