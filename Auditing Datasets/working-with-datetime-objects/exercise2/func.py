"""
A simple function comparing datetime objects.

Author: Julissa Bonilla
Date:   4/5/2022
"""
import datetime


def is_before(d1,d2):
    """
    Returns True if event d1 happens before d2.
    
    Values d1 and d2 can EITHER be date objects or datetime objects.If a date object,
    assume that it happens at midnight of that day. 
    
    Parameter d1: The first event
    Precondition: d1 is EITHER a date object or a datetime object
    
    Parameter d2: The first event
    Precondition: d2 is EITHER a date object or a datetime object
    """
    if type(d1)==datetime.datetime:
        if type(d2)==datetime.datetime:
            return d1<d2
        else:
            d2=datetime.datetime(d2.year,d2.month,d2.day,0,0,0,0)
            return d1<d2
    else:
        d1=datetime.datetime(d1.year,d1.month,d1.day,0,0,0,0)
        if type(d2)==datetime.datetime:
            return d1<d2
        else:
            d2=datetime.datetime(d2.year,d2.month,d2.day,0,0,0,0)
            return d1<d2