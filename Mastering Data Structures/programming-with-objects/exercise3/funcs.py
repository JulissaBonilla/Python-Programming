"""
Functions demonstrating string methods.

Neither this module nor any of these functions should import the introcs module.
In addition, you are not allowed to use loops or recursion in either function.

Author: Julissa Bonilla
Date: 3/5/22
"""


def first_in_parens(s):
    """
    Returns: The substring of s that is inside the first pair of parentheses.
    
    The first pair of parenthesis consist of the first instance of character
    '(' and the first instance of ')' that follows it.
    
    Examples: 
        first_in_parens('A (B) C') returns 'B'
        first_in_parens('A (B) (C)') returns 'B'
        first_in_parens('A ((B) (C))') returns '(B'
    
    Parameter s: a string to check
    Precondition: s is a string with a matching pair of parens '()'.
    """
    open=s.find('(')+1
    close=s[open:].find(')')+open
    return s[open:close]
    
def isnetid(s):
    """
    Returns True if s is a valid Cornell netid.
    
    Cornell network ids consist of 2 or 3 lower-case initials followed by a 
    sequence of digits.
    
    Examples:
        isnetid('wmw2') returns True
        isnetid('2wmw') returns False
        isnetid('ww2345') returns True
        isnetid('w2345') returns False
        isnetid('WW345') returns False
    
    Parameter s: the string to check
    Precondition: s is a string
    """
    if s[:3].isalpha() and s[:3].islower():
        init=3
        isdigSeq=s[init:].isnumeric()
    elif s[:2].isalpha() and s[:2].islower():
        init=2
        isdigSeq=s[init:].isnumeric()
    else: return False
    return isdigSeq