"""
Module demonstrating how to write functions with objects.

This module contains two versions of the same function.  One version returns a new
value, while other modifies one of the arguments to contain the new value.

Author: Julissa Bonilla
Date: 3/4/22
"""
import clock


def add_time1(time1, time2):
    """
    Returns the sum of time1 and time2 as a new Time object
    
    DO NOT ALTER time1 or time2, even though they are mutable
    
    Examples: 
        The sum of 12hr 13min and 13hr 12min is 25hr 25min 
        The sum of 1hr 59min and 3hr 2min is 5hr 1min 
    
    Parameter time1: the starting time
    Precondition: time1 is a Time object
    
    Parameter time2: the time to add
    Precondition: time2 is a Time object
    """
    assert type(time1)==clock.Time
    assert type(time2)==clock.Time
    time3=clock.Time
    sumMin=time1.minutes+time2.minutes
    time3mins=sumMin
    time3hours=0
    if sumMin>59:
      time3hours=sumMin//60
      time3mins=sumMin%60
    time3=clock.Time(time1.hours+time2.hours+time3hours,time3mins)
    return time3


def add_time2(time1, time2):
    """
    Modifies time1 to be the sum of time1 and time2
    
    DO NOT RETURN a new time object.  Modify the object time1 instead.
    
    Examples: 
        The sum of 12hr 13min and 13hr 12min is 25hr 25min 
        The sum of 1hr 59min and 3hr 2min is 5hr 1min 
    
    Parameter time1: the starting time
    Precondition: time1 is a Time object
    
    Parameter time2: the time to add
    Precondition: time2 is a Time object
    """
    assert type(time1)==clock.Time
    assert type(time2)==clock.Time
    sumMin=time1.minutes+time2.minutes
    hours=0
    if sumMin>59:
      hours=sumMin//60
      sumMin=sumMin%60
    time1.hours=time1.hours+time2.hours+hours
    time1.minutes=sumMin

