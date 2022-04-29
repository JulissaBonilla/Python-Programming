"""
A function to find all instances of a substring.

This function is not unlike a 'find-all' option that you might see in a text editor.

Author: Julissa Bonilla
Date: 2/24/22
"""
import introcs


def findall(text,sub):
    """
    Returns the tuple of all positions of substring sub in text.
    
    If sub does not appears anywhere in text, this function returns the empty tuple ().
    
    Examples:
        findall('how now brown cow','ow') returns (1, 5, 10, 15)
        findall('how now brown cow','cat') returns ()
        findall('jeeepeeer','ee') returns (1,2,5,6)
    
    Parameter text: The text to search
    Precondition: text is a string
    
    Parameter sub: The substring to search for
    Precondition: sub is a nonempty string
    """

    result=()
    pos=0
    
    for x in range(0,len(text)):
        
        hit=introcs.find_str(text,sub)
        if hit<0:break
        pos=pos+hit
        if hit<0: 
            result=result+(pos-1,)
            break
        result=result+(pos,)
        text=text[hit+1:]
        pos=pos+1
        
        
    return result
