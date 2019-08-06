#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Readme!

Run from terminal/command line by:
    cd to inside the directory where this file is located
    python -i CreateReport.py
    >>>CreateReport(logpath,daterange)
logpath should be relative (if the log is called "log.txt" and is in folder B 
which is in Folder A where this file is, then the path should be 'B/log.txt')

Tested on the supplied logs (examplelog 1-3) in Ubuntu 16.04.

"""
import pandas as pd
from datetime import datetime as dt

#Helper function to convert string to datetime object and then to unix time 
def ToDT(datetimestring):
    if(len(datetimestring) == 22):
         return dt.strptime(datetimestring, '%Y-%m-%d %H:%M:%S%Z').timestamp()
    else:
        return dt.strptime(datetimestring, '%Y-%m-%d %H:%M:%S').timestamp()


#Report creation function
def CreateReport(logpath, daterange):
    log = pd.read_csv(logpath)

    reportdf = pd.DataFrame(columns=['url','page views','visitors']) #The actual report
    if len(log) == 0 or daterange is None:
        return reportdf #Nothing to show, return empty report with the column titles only
    else:
        reqtimestart = ToDT(daterange[:19])
        reqtimeend = ToDT(daterange[:11]+daterange[22:])
        
        #Dropping the rows with timestamps outside the requested date-range   
        for l in log['timestamp']:
            if ToDT(l) < reqtimestart or ToDT(l) > reqtimeend:
                idx = log[log['timestamp']==l].index
                log.drop(idx, inplace=True)                    
            
        urlarr = list(set(log['url'])) #set of unique url values from the log

        reportdf = pd.DataFrame(columns=['url','page views','visitors']) #The actual report
        reportdf['url'] = urlarr #urls column
        reportdf.fillna(0)

        #Finding number of page views and adding to the report
        for r in reportdf['url']:
            idx = reportdf[reportdf['url'] == r].index
            reportdf.loc[idx,'page views'] = log.url.value_counts()[r]
            
        
        #Finding number of unique visitors for each page and adding to the report
        for r in reportdf['url']:
            uni = log.loc[log['url']==r].userid.nunique() #Number of unique visitors for the rows containing a particular url
            idx = reportdf[reportdf['url'] == r].index
            reportdf.loc[idx,'visitors'] = uni
            

        return reportdf

