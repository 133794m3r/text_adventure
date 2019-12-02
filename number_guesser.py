#!/usr/bin/python3
#Importing random so that I can have a RNG
import random
#importing sys so that I can take arguments.
import sys
#importing getop so that I can read command line options.
import getopt

# this function will return a number between the minimum and the maximum.
# It takes two arguments min and max.
def rand(min,max):
    # We try to return them the value they want.
    try:
        return int(random.random() * (max-min)) + min
    #if they don't supply us with valid inputs then we give them the error.
    except ValueError as error:
        print(error)

# Here's the main function that handles the number guessing. It keeps going and gives them hints.
def guesser(min,max):
    # I initialize the value to 0.
    num=0;
    # The correct answer is a random number in the range given to this function.
    ans=rand(min,max)
    # The guesses counter.
    guesses=0;
    # This tells them the range of numbers they're guessing.
    # The {} tells python that when format is passed to it to put the variable passed to it from format
    # into the function.
    print('Guess a number from {} to {}'.format(min,max))
    # While the number is not equal to the answer we keep looping.
    while num != ans:
        print('What is your guess?',end=' ')
        # we have a try catch here in case they enter invalid data.
        try:
            num=int(input())
        # If they dont' give us a valid number we tell them.       
        except ValueError as error:
            print('Your guess was not a valid number. In addition we got this error "{}"'.format(error))
        # If the number they give us is outside of the valid range we tell them.            
        if (num > max or num < min):
        # Tell them that their input wasn't in the range.
            print(f'Your guess {num} was not in the valid range {min} to {max}')
        # else if the number is greater than the correct one tell them it was too high.            
        elif num > ans:
            print('Your guess was too high')
        # otherwise we tell them that their guess was too low.
        else:
            print('Your guess was too low.')
        # increment their guess counter.            
        guesses+=1
    #Tell them that they got it right along with how many guesses it        
    print(f'Correct the number was {num}, and it only took you {guesses}')
    
# The primary function that handles the number guessing and seeing if the user is done.    
def number_guesser(min,max):
    loop=True
    response='';
    #another loop, while the variable loop is true we keep on going.
    while loop == True:
        #run the guesser program with our min and max variables.
        guesser(min,max)
        # Ask them if they'd like to play again.
        print('Would you like to play again? Y/N',end=' ')
        #set their response to the response variable.
        response=input()
        # see if it's any of the values after the "in" keyword. If so keep going.
        if response in ('Y','Yes','y','yes'):
            loop=True
        # otherwise we're done with the loop and it's time to leave it.            
        else:
            loop=False

# this function just displays usage instructions that's it.        
def help():
    print("This script is a random number guesser with the following arguments",end=" ")
    print("-m|--min -n|--max -h|--help",end=" ")
    print("Min is the minimum number for the guesser to guess. Max is the maximum number in the range. Help will show this message and exit. Minimum and maximum must be positive whole numbers. All arguments are optional.")
    
    
# The main function just like C is the first one that's ran by default.    
def main(argv=None):
    #see if argv is type None
    if argv is None:
        #it is so we import the argv aka the arguments string from the console.
        argv=sys.argv
    # try to parse the arguments.
    try:
    # This sets the options to opt and the arguments to args.
    # further we're saying that the arguments m and n both require an argument
    # whereas h or the help argument does not.
        opts, args = getopt.getopt(argv[1:],"m:n:h",["min","max","help"])
    # something went majorly wrong.        
    except getopt.getOptError as error:
        #tell them what went wrong.
        print(str(err))
    #print the help/usage string.        
        help()
    #exit with an error        
        sys.exit(2)
    #initialize the variables with default values.        
    min=1
    max=20
    showhelp=False
    # do a loop getting the values from the opts list.
    # We get the options and arguments from it. It is a 2d "array" if you're thinkng of other languages.
    # for example let's say that you included the argument "-m 1"
    # it'd show up as ["-m","1"] for the list at the index that we're at from the opts list.
    for opt,arg in opts:
        # see if opt is one of these to tell it to call the help function.
        if opt in ("-h","--help"):
            help()
            #exit normally.
            sys.exit()
        # they set the minimum value. Here I'm making sure that it's a positive number by calling abs.
        # further            
        elif opt in ("-m","--min"):
            # just incase they did something wrong. Tell them that they did and don't crash it.
            try:
                # if it worked we take the absolute value of their number as an integer.
                min=abs(int(arg))
            except ValueError as error:
                # tell them their error.
                print('You had this error "{}"'.format(error))
                showhelp=True
        # this is the same as above but for the max option.                
        elif opt in ("-n","--max"):
            try:        
                max=abs(int(arg))
            except ValueError as error:
                print('You had this error "{}"'.format(error))
                showhelp=True              
        else:
            assert False
    # if they screwed up show the help message and exit.            
    if showhelp == True:
        help()
    # we tell it to exit with 2 as it was an issue with the command line arguments.        
        sys.exit(2)
    else:
        number_guesser(min,max)
#here is where we make sure that the main function is called.                
if __name__ == "__main__":
    main()
                
