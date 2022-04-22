"""
A module with an incomplete function.

This function was implemented using the backwards-design technique.

Author: Julissa Bonilla
Date: 1/13/22
"""
import introcs


def second_in_list(s):
    """
    Returns: the second item in comma-separated list
    
    The final result should not have any whitespace around the edges.
    
    Example: second_in_list('apple, banana, orange') returns 'banana'
    Example: second_in_list('  do  ,  re  ,  me  ,  fa  ') returns 're'
    Example: second_in_list('z,y,x,w') returns 'y'
    
    Parameter s: The list of items
    Precondition: s is a string of at least three items separated by commas.
    """
    assert type(s) == str, 'Precondition violation'
    assert introcs.count_str(s,',')>=2 , 'Precondition violation'
    c1=introcs.find_str(s,',')
    c2=introcs.find_str(s,',',c1+1)
    slice= s[c1+1:c2]
    result = introcs.strip(slice)
    return result
