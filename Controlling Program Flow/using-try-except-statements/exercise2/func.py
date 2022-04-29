"""  
A function to test for floats in European format

Author: Julissa Bonilla
Date: 2/18/22
"""
import introcs


def iseurofloat(s):
    """
    Returns True if s is a float in European format.  Returns False otherwise.
    
    In European format, a comma is used in place of a decimal point.  So '12,5' stands
    for 12.5, '0,12' stands for 0.12 and so.  Formally, a string is in European format
    if it is of the form <d1>,<d2> where d1 and d2 are ints (and d2 >= 0).  See
        
        https://en.wikipedia.org/wiki/Decimal_separator
    
    for more information.
    
    This function does not recognize floats in scientific notation (e.g. '1e-2').
    
    Examples: 
        iseurofloat('12,5') returns True
        iseurofloat('-12,5') returns True
        iseurofloat('12') returns False
        iseurofloat('12,-5') returns False
        iseurofloat(',5') returns False
        iseurofloat('apple') returns False
        iseurofloat('12,5.3') returns False
        iseurofloat('12,5,3') returns False
        iseurofloat('1e-2') returns False
    
    Parameter s: The string to check
    Precondition: s is a string
    """
    # You MAY NOT use conditionals anywhere in this function.
    try:
        """
        x= str(s)
        c=index_str(s,',')
        print(c)
        print(s[:c-1])
        len(s[:c-1])>0
        d1=introcs.isint(s[:c-1])
        print(d1)
        d2=introcs.isint(s[c:])
        print(s[c:])
        print(d2)
        return True
        
        s=introcs.replace_str(s, ',', '.')
        introcs.find_str(s, '.')>0
        introcs.isfloat(s)
        return True
        """
        x= str(s)
        c=introcs.index_str(s,',')
        l=s[:c]
        d1=1/(introcs.isint(l))
        r=s[c+1:]
        neg=1/introcs.isdigit(r)
        d2=1/(introcs.isint(r))
        return True
        
    except:
        return False
        
