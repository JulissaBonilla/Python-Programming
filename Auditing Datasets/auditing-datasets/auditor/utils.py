"""
Module providing utility functions for this project.

These functions are general purpose utilities used by other modules in this project.
Some of these functions were exercises in early course modules and should be copied
over into this file.

The preconditions for many of these functions are quite messy.  While this makes writing 
the functions simpler (because the preconditions ensure we have less to worry about), 
enforcing these preconditions can be quite hard. That is why it is not necessary to 
enforce any of the preconditions in this module.

Author: Julissa Bonilla
Date: 4/7/2022
"""
import csv
import json
import datetime
import pytz
from dateutil.parser import parse



def read_csv(filename):
    """
    Returns the contents read from the CSV file filename.
    
    This function reads the contents of the file filename and returns the contents as
    a 2-dimensional list. Each element of the list is a row, with the first row being
    the header. Cells in each row are all interpreted as strings; it is up to the 
    programmer to interpret this data, since CSV files contain no type information.
    
    Parameter filename: The file to read
    Precondition: filename is a string, referring to a file that exists, and that file 
    is a valid CSV file
    """
    
    f=open(filename,"r")
    wrapper=csv.reader(f)

    contents=[]
    for row in wrapper:
        num = []
        for i in range(len(row)):
            num.append(str(row[i]))
        contents.append(num)
    f.close()
    return contents

def write_csv(data,filename):
    """
    Writes the given data out as a CSV file filename.
    
    To be a proper CSV file, data must be a 2-dimensional list with the first row 
    containing only strings.  All other rows may be any Python value.  Dates are
    converted using ISO formatting. All other objects are converted to their string
    representation.
    
    Parameter data: The Python value to encode as a CSV file
    Precondition: data is a  2-dimensional list of strings
    
    Parameter filename: The file to read
    Precondition: filename is a string representing a path to a file with extension
    .csv or .CSV.  The file may or may not exist.
    """
    f=open(filename,"w")
    wrapper=csv.writer(f)
    for x in range(len(data)):
        wrapper.writerow(data[x])
    f.close()

def read_json(filename):
    """
    Returns the contents read from the JSON file filename.
    
    This function reads the contents of the file filename, and will use the json module
    to covert these contents in to a Python data value.  This value will either be a
    a dictionary or a list. 
    
    Parameter filename: The file to read
    Precondition: filename is a string, referring to a file that exists, and that file 
    is a valid JSON file
    """
    f=open(filename,'r')
    data=json.load(f)
    f.close()
    return data


def str_to_time(timestamp,tz=None):
    """
    Returns the datetime object for the given timestamp (or None if stamp is invalid)
    
    This function should just use the parse function in dateutil.parser to
    convert the timestamp to a datetime object.  If it is not a valid date (so
    the parser crashes), this function should return None.
    
    If the timestamp has a timezone, then it should keep that timezone even if
    the value for tz is not None.  Otherwise, if timestamp has no timezone and 
    tz if not None, this this function will assign that timezone to the datetime 
    object. 
    
    The value for tz can either be a string or a time OFFSET. If it is a string, 
    it will be the name of a timezone, and it should localize the timestamp. If 
    it is an offset, that offset should be assigned to the datetime object.
    
    Parameter timestamp: The time stamp to convert
    Precondition: timestamp is a string
    
    Parameter tz: The timezone to use (OPTIONAL)
    Precondition: tz is either None, a string naming a valid time zone,
    or a time zone OFFSET.
    """
    # HINT: Use the code from the previous exercise and update the timezone
    # Use localize if timezone is a string; otherwise replace the timezone if not None
    try:
        dt=parse(timestamp)
    except:
        return None

    if dt.tzinfo != None:
        return dt
    elif dt.tzinfo == None:
        if tz == None:
            return dt
        elif tz != None:
            if isinstance(tz, str) == False:
                dtnu = dt.replace(tzinfo=tz)
                return dtnu

        if isinstance(tz, str) == True:
            
            tza = pytz.timezone(tz)
            
            dtnu = dt.replace(tzinfo=tza)
            
            dtloc = tza.localize(dt)


            return dtloc


def daytime(time,daycycle):
    """
    Returns true if the time takes place during the day.
    
    A time is during the day if it is after sunrise but before sunset, as
    indicated by the daycycle dicitionary.
    
    A daycycle dictionary has keys for several years (as int).  The value for
    each year is also a dictionary, taking strings of the form 'mm-dd'.  The
    value for that key is a THIRD dictionary, with two keys "sunrise" and
    "sunset".  The value for each of those two keys is a string in 24-hour
    time format.
    
    For example, here is what part of a daycycle dictionary might look like:
    
        "2015": {
            "01-01": {
                "sunrise": "07:35",
                "sunset":  "16:44"
            },
            "01-02": {
                "sunrise": "07:36",
                "sunset":  "16:45"
            },
            ...
        }
    
    In addition, the daycycle dictionary has a key 'timezone' that expresses the
    timezone as a string. This function uses that timezone when constructing
    datetime objects from this set.  If the time parameter does not have a timezone,
    we assume that it is in the same timezone as the daycycle dictionary
    
    Parameter time: The time to check
    Precondition: time is a datetime object
    
    Parameter daycycle: The daycycle dictionary
    Precondition: daycycle is a valid daycycle dictionary, as described above
    """
    # HINT: Use the code from the previous exercise to get sunset AND sunrise
    # Add a timezone to time if one is missing (the one from the daycycle)
    year = time.year
    year_dictionary = daycycle[str(year)]
    
    month = str(time.month)
    if len(month) < 2:
        month = "0" + month
    
    day = str(time.day)
    if len(day) < 2:
        day = "0" + day 
        

    date = month + "-" + day
    
    month_dictionary = year_dictionary[date]
    
    
    sunrise = month_dictionary['sunrise']
    sunrise_hours = sunrise[0:2]
    if sunrise_hours[0] == '0':
        sunrise_hours = (sunrise_hours[1:2])
    
    sunrise_minutes = sunrise[3:5]
    if sunrise_minutes[0] == '0':
        sunrise_minutes = (sunrise_minutes[1:])
        
        
    sunset = month_dictionary['sunset']
    sunset_hours = sunset[0:2]
    if sunset_hours[0] == '0':
        sunset_hours = (sunset_hours[1:2])
        
    sunset_minutes = sunset[3:5]
    if sunset_minutes[0] == '0':
        sunset_minutes = (sunset_minutes[1:])
        

   
    tzcheck = time.tzinfo != None              
    if tzcheck == True:
        tz = pytz.timezone('America/New_York')                                                                                
        sunrise_naive = datetime.datetime(int(year),int(month),int(day),int(sunrise_hours),int(sunrise_minutes))        
        sunrise = tz.localize(sunrise_naive)                                                                                   

        sunset_naive = datetime.datetime(int(year),int(month),int(day),int(sunset_hours),int(sunset_minutes))
        sunset = tz.localize(sunset_naive)

        now = time

    if now <= sunrise:
       
        return False

    if now > sunrise:
        
        if now < sunset:
            
            return True

        if now >= sunset:
            
            return False


def get_for_id(id,table):
    """
    Returns (a copy of) a row of the table with the given id.
    
    Table is a two-dimensional list where the first element of each row is an identifier
    (string).  This function searches table for the row with the matching identifier and
    returns a COPY of that row. If there is no match, this function returns None.
    
    This function is useful for extract rows from a table of pilots, a table of instructors,
    or even a table of planes.
    
    Parameter id: The id of the student or instructor
    Precondition: id is a string
    
    Parameter table: The 2-dimensional table of data
    Precondition: table is a non-empty 2-dimension list of strings
    """
    for row in range(1,len(table)):
        for col in range(len(table[0])):
            if id in table[row][col]:
                return table[row]
