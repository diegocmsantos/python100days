'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
import os
import urllib.request
import re

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

# for you to code:

def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object. 
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    rex = r"(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}).+(Shutdown initiated)"
    match = re.search(rex, line)
    if match is not None:
        date_str = match.group(1)
        return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
    return None

def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the 
       timedelta between the first and last one. 
       Return this datetime.timedelta object.'''
    datetimes = []
    for line in loglines:
        datetime_item = convert_to_datetime(line)
        if datetime_item:
            datetimes.append(datetime_item)
    return datetimes[1] - datetimes[0]

with open(logfile) as f:
    loglines = f.readlines()
    print(time_between_shutdowns(loglines))