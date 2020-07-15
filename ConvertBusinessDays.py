
'''
Authored by Heather Lansdell 

Creation of Custom Business Day class. Allows calling as a instance as MyCalendar() to calculate a Custom Business Day Offest according to desired calendars. The Holidays above are only those observed 
for a project I was working on. Very easy to adapt for the pandas USFederalCalendar or any user desired Holidays. Just import the required holiday on line 4, or create a custom holiday like on line 8. 
The nearest_workday observed is an awesomed function included 
in the holiday package.   Documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-holiday

The way this is built allows the user to specify a start and end date and map the business days for the next 5 years. Leap years are handled, weekdays are handled. A file is returned that gives the date, it's calendar day
per cycle, business day per cycle, and if it is a business day or not, so that it can act as a reference for many different users. 
For my project, these defined holidays and weekends are 'non business days'. 
This functionality was used to not only forecast future business days, but to return where we are in a current cycle, so that when a program ran via task scheduler,
certain downstream tasks could launch according to where they fell in the calendar or business day cycle. 

I wrote this because most functionality I saw pertained to counting business days per cycle versus calendar days. I had yet to find something that programmatically tracked where you were in a cycle as defined by custom parameters.

MyCalendar Holidays are defined as: New Years Day, Memorial Day, Independence Day, Labor Day, Thanksgiving Day, Christmas Day. The nearest workday is used when they fall on a weekend. 
'''  



import pandas as pd             
import datetime as dt
from datetime import date
import calendar
import numpy as np

from pandas.tseries.offsets import MonthEnd
from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday, nearest_workday,USMemorialDay, USLaborDay, USThanksgivingDay



'''
#For Dev backdating runs
cycle = dt.datetime.strptime('2020 12 01', '%Y %m %d')
cycle=cycle.date()
'''


class MyCalendar(AbstractHolidayCalendar):
    rules = [
        Holiday('NewYearsDay', month=1, day=1, observance=nearest_workday),
       
        USMemorialDay,
        Holiday('USIndependenceDay', month=7, day=4, observance=nearest_workday),
        USLaborDay,
        USThanksgivingDay,
        Holiday('Christmas', month=12, day=25, observance=nearest_workday)] 


def bus_day_convertor(date_in_cycle):
    
  
    mon_end=(date_in_cycle+MonthEnd(1)).date()
    days_in_mon=(mon_end-date_in_cycle).days+1
   
    hols=list(MyCalendar().holidays(start=date_in_cycle,end=mon_end).to_pydatetime())
    year=date_in_cycle.year
    month=date_in_cycle.month
    
    i=0
    cal_days=[]
    bus_days=[]
    busness_day_boolean=[]
    for x in range(1,days_in_mon+1):
        cal_days.append(x)
        try:
            weekday = calendar.weekday(year, month, x)
            hol_days=[day.date().day for day in hols]
        except ValueError:
            pass
        if (weekday < calendar.SATURDAY) and (x not in hol_days):
            i+=1
            bus_days.append(i)
            busness_day_boolean.append('TRUE')
        else:
            i=i            
            bus_days.append(i)
            busness_day_boolean.append('FALSE')
    
    datelist=pd.date_range(date_in_cycle,periods=days_in_mon).tolist()
    
    df=pd.DataFrame()        
    df['DATE']=datelist        
    df['CALENDAR DAY PER CYCL']=cal_days
    df['BUSINESS DAY PER CYCLE']=bus_days
    df['BUSINESS DAY?']=busness_day_boolean
    return df


def main():
  
    startyear=2020
    startmonth=7
    endyear=2027
    endmonth=12
    cycles=[dt.date(m//12, m%12+1, 1) for m in range(startyear*12+startmonth-1, endyear*12+endmonth)]
    
    dfs=[]
        
    for date_in_cycle in cycles:
        df=bus_day_convertor(date_in_cycle)
        dfs.append(df)
        
    final_df=pd.concat(dfs)
        
    final_df.to_csv('BusinessDaysinRange.csv',index=None, header=final_df.columns.values)
    

if __name__ == '__main__':
   main()

'''
Example Usage of Logic:

def bus_day_convertor(date_in_cycle):
        
    mon_beg=(date_in_cycle-MonthBegin(1)).date()
    day_in_mon_so_far=(date_in_cycle-mon_beg).days+1
    
    hols=list(MyCalendar().holidays(start=mon_beg,end=date_in_cycle).to_pydatetime())
    year=date_in_cycle.year
    month=date_in_cycle.month
    day=date_in_cycle.day
    
    bus_day_counter=0
    for x in range(1,day_in_mon_so_far):
        try: #two counters are used, one for weekdays, one for business days
            weekday = calendar.weekday(year, month, x) #get integer for weekday
            hol_days=[day.date().day for day in hols]    #get integer from holiday list 
        except ValueError:
            pass
        if (weekday < calendar.SATURDAY) and (day not in hol_days):
            bus_day_counter+=1
        else:
            bus_day_counter=bus_day_counter           
                        
    return bus_day_counter


def calc_due_tasks(outline): 
    
    now = dt.datetime.now()  
    
    # what day is it today?
    today=now.date()
    # what day is that in calendar day per month?
    calday_per_mon=now.day    
    #what day is that in calendar day per year?
    calday_per_year=now.timetuple().tm_yday    

    #what day is that in business day per month?
    busday_per_mon=bus_day_convertor(today)

	due_tasks=[]
    
    for task,task_dict in outline.items():
    
    	do desired functions....'''