"""
Module to demonstrate keyword expansion.

Author: Julissa Bonilla
Date: 3/20/22
"""
import math


def circ_area(**kwd):    # The parameter is MISSING.  Add it back. 
    """
    Returns the area of the specified circle, defined by the keywords in kwd
    
    The area of a circle is PI r*r where r is the radius
    
    The circle may be specified by 'radius' or 'diameter', but not both.  This function
    should intentionally crash (with an AssertionError) if neither 'radius' nor 'diameter' 
    are specified, or if they both are.
    
    Any keyword arguments other than 'radius' or 'diameter' are ignored.
    
    Examples: 
        circ_area(radius=3) returns approx 28.27433
        circ_area(diameter=4) returns approx 12.56637
        circ_area(radius=3,foo=20) returns approx 28.27433
        circ_area() crashes with AssertionError
        circ_area(radius=2,diameter=4) crashes with AssertionError
    
    Parameter kwd: the function keyword arguments
    Precondition: the arguments are all numbers (int or float)
    """
    keys = list(kwd.keys())
    assert ('radius' in keys or 'diameter' in keys)
    assert not ('radius' in keys and 'diameter' in keys),"both"
    assert not(len(keys)==0),"empty"
    for x in keys:
        if x == "radius":
            return math.pi * kwd[x] * kwd[x]
        if x=="diameter":
            r= kwd[x]/2
            return math.pi * r * r