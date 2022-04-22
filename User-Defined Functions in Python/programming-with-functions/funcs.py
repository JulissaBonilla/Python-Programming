"""
The functions for the course project.

Author: Julissa Bonilla
Date: 1/14/22
"""
import introcs
def matching_parens(s):
    """
    Returns True if the string s has a matching pair of parentheses.

    A matching pair pair of parentheses is an open parens '(' followed by a closing
    parens ')'.  Any thing can be between the two pair (including other parens).

    Example: matching_parens('A (B) C') returns True
    Example: matching_parens('A )B( C') returns False

    Parameter s: The string to check
    Precondition: s is a string (possibly empty)
    """
    assert type(s) == str
    # Search for the first open parens '('
    firstOpen=introcs.find_str(s,'(')
    # Search for the first close parens ')' AFTER the open parens
    firstClosed=introcs.find_str(s,')',firstOpen)
    
    # Compare both searches to -1 and return True if BOTH are not -1
    return firstOpen!=-1 and firstClosed!=-1

def first_in_parens(s):
    """
    Returns: The substring of s that is inside the first pair of parentheses.

    The first pair of parenthesis consist of the first instance of character
    '(' and the first instance of ')' that follows it.

    Example: first_in_parens('A (B) C') returns 'B'
    Example: first_in_parens('A (B) (C)') returns 'B'
    Example: first_in_parens('A ((B) (C))') returns '(B'

    Parameter s: a string to check
    Precondition: s is a string with a matching pair of parens '()'.
    """
    assert type(s) == str
    assert matching_parens(s)==True
    firstOpen=introcs.find_str(s,'(')
    firstClosed=introcs.find_str(s,')',firstOpen)
    return str(s[firstOpen + 1:firstClosed])