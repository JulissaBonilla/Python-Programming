"""
Module demonstrating an input-driven while loop

There is no test script for this module.  Run this module as a script to test it.

Author: Julissa Bonilla
Date: 2/24/22
"""


def count_inputs():
    """
    Returns the number of times the user chose to continue.
    
    This function repeated asks the user
        
        Keep going [y/n]? 
    
    If the user answers 'y', the function adds one to a counter and keeps going.
    If the user answers 'n', the function quits and returns the number of times
    that the user answered 'y'.  If the user answers anything else, the function
    responds with
        
        Answer unclear. Use 'y' or 'n'.
    
    It will not quit in this case, but it will not add to the counter either.
    """
    # Create a counter accumulator
    count=0
    # Create a variable 'going' to control the loop
    going=True
    # While the user has not told us to stop
    count=0
    going=True
    while going:
        # Get the input from the user
        answer=input('Keep going [y/n]? ')
        # Respond with error message if input is bad
        if answer!='y' and answer!='n':
            print('Answer unclear. Use \'y\' or \'n\'.')
        # Update counter if input is 'y'
        if answer=='y':
            count=count+1
        if answer == 'n':
            return count


# Script code to test the function
# DO NOT MODIFY BELOW THIS LINE
if __name__ == '__main__':
    result = count_inputs()
    plural = ' time.' if result == 1 else ' times.'
    print("You answered 'y' "+str(result)+plural)
