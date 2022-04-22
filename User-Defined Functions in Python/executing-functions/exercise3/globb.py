"""  
A module to demonstrate global variables.

Author: Julissa Bonilla
Date: 1/3/2022
"""

# The global variable
VAR = 1

def next():
    """
    Returns and increments the value of VAR.
    """
    global VAR
    result = VAR
    VAR = VAR+1
    return result