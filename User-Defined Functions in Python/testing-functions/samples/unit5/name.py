"""
The debug version of the module name

In this module we have added print statements after every assignment. These allow us
to 'visualize" the program while it is running, and hence isolate the error. However,
they will eventually need to be removed when we find the error.

Author: Walker M. White
Date:   February 14, 2019
"""
import introcs


def last_name_first(n):
    """
    Returns: copy of n but in the form 'last-name, first-name'

    We assume that n is just two names (first and last).  Middle names are
    not supported.

    Examples:
        last_name_first('Walker White') returns 'White, Walker'
        last_name_first('Walker      White') returns 'White, Walker'

    Parameter n: the person's name
    Precondition: n is in the form 'first-name last-name' with one or more
    spaces between the two names. There are no spaces in either <first-name>
    or <last-name>
    """
    print(n)
    
    end_first = introcs.find_str(n,' ')
    print(end_first)
    
    first = n[:end_first]
    print(first)
    
    last  = introcs.strip(n[end_first+1:])
    print(last)
    
    return last+', '+first
