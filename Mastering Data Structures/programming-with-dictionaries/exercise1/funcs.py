"""
Module demonstrating immutable functions on dictionaries

All of these functions make use of accumulators.

Author: Julissa Bonilla
Date: 3/17/22
"""


def average_grade(adict):
    """
    Returns the average grade among all students.

    The dictionary adict has netids for keys and numbers 0-100 for values.
    These represent the grades that the students got on the exam.  This function
    averages those grades and returns a value.

    Examples:
        average_grade({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) returns (55+90+86)/3 = 77
        average_grade({'wmw2' : 55}) returns 55
        average_grade({}) returns 0
    
    Parameter adict: the dictionary of grades
    Precondition: adict is dictionary mapping strings to ints
    """
    rawGrade=list(adict.values())
    sum=0
    num=0
    if len(adict)<1:
        return 0
    for x in rawGrade:
        sum=sum+x
        num=num+1
    return sum/num


def letter_grades(adict):
    """
    Returns a new dictionary with the letter grades for each student.
    
    The dictionary adict has netids for keys and numbers 0-100 for values. These
    represent the grades that the students got on the exam. This function returns a 
    new dictionary with netids for keys and letter grades (strings) for values.
    
    Our cut-off is 90 for an A, 80 for a B, 70 for a C, 60 for a D. Anything below 60 
    is an F.
    
    Examples:  
        letter_grades({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) returns
            {'wmw2' : 'F, 'abc3' : 'A', 'jms45': 'B'}.
        letter_grades({}) returns {}
    
    Parameter adict: the dictionary of grades
    Precondition: adict is dictionary mapping strings to ints
    """
    if len(adict)<1:
        return {}
    x=()
    count=0
    for stud in adict:
        if adict[stud] >= 90:
            student=(stud,'A'),
        elif adict[stud] >= 80 and adict[stud]<90:
            student=(stud,'B'),
        elif adict[stud] >= 70 and adict[stud]<80:
            student=(stud,'C'),
        elif adict[stud] >= 60 and adict[stud]<70:
            student=(stud,'D'),
        else:
           student=(stud,'F'),
        x=x+student
        count=count+1
    return dict(x)
