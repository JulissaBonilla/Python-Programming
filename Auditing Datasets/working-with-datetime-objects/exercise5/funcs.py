"""
Functions for parsing time values and determining daylight hours.

Both of these functions will be used in the main project.  You should hold on to them.

Author: Julissa Bonilla
Date:  4/5/2022
"""
import datetime
import pytz
from dateutil.parser import parse

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
