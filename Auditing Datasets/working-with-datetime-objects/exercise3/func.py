"""
A simple function computing time elapsed

Author: Julissa Bonilla
Date:   4/5/2022
"""
import datetime


def past_a_week(d1,d2):
    """
    Returns True if event d2 happens at least a week (7 days) after d1.
    
    If d1 is after d2, or less than a week has passed, this function returns False.
    Values d1 and d2 can EITHER be date objects or datetime objects.If a date object,
    assume that it happens at midnight of that day. 
    
    Parameter d1: The first event
    Precondition: d1 is EITHER a date objects or a datetime object
    
    Parameter d2: The first event
    Precondition: d2 is EITHER a date objects or a datetime object
    """
    if type(d1)==datetime.datetime:
        if type(d2)==datetime.datetime:
            return (d2-d1)>=datetime.timedelta(days=7)
        else:
            d2=datetime.datetime(d2.year,d2.month,d2.day,0,0,0,0)
            return (d2-d1)>=datetime.timedelta(days=7)
    else:
        d1=datetime.datetime(d1.year,d1.month,d1.day,0,0,0,0)
        if type(d2)==datetime.datetime:
            return (d2-d1)>=datetime.timedelta(days=7)
        else:
            d2=datetime.datetime(d2.year,d2.month,d2.day,0,0,0,0)
            return (d2-d1)>=datetime.timedelta(days=7)
    
