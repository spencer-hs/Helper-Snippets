# Python Helper Snippets


All of the following are snippets used to perform useful data tasks

  - Forecasting Business Days in Production Cycles/Tracking Where you are in Production Cycle (ConvertBusinessDays)
  - File Comparison that creates a summary report of differences (FileCompare)
  - Searching for membership between multiple groups from passed excel/csv files (List_membership_check)
  - Searchs every file with a paticukar extension and subs one string for another (StringReplacement)
  - Excel ID conversion for subject abstraction in trials (SubjectIDExcelConversion)
  - Stripping Characters with regex (character_remover_python)


*All of the following snippets require Pandas.

### ConvertBusinessDays
Creation of Custom Business Day class. Allows calling as a instance as MyCalendar() to calculate a Custom Business Day Offest according to desired calendars. The Holidays above are only those observed for a project I was working on. Very easy to adapt for the pandas USFederalCalendar or any user desired Holidays. Just import the required holiday on line 4, or create a custom holiday like on line 8. The nearest_workday observed is an awesomed function included in the holiday package. 

The way this is built allows the user to specify a start and end date and map the business days for the next 5 years. Leap years are handled, weekdays are handled. A file is returned that gives the date, it's calendar day per cycle, business day per cycle, and if it is a business day or not, so that it can act as a reference for many different users. 

For my project, these defined holidays and weekends are 'non business days'. 
This functionality was used to not only forecast future business days, but to return where we are in a current cycle, so that when a program ran via task scheduler, certain downstream tasks could launch according to where they fell in the calendar or business day cycle. 

I wrote this because most functionality I saw pertained to counting business days per cycle versus calendar days. I had yet to find something that programmatically tracked where you were in a cycle as defined by custom parameters.

Requirements:
* [Pandas Holiday](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-holiday) 
* [Pandas OffSet MonthEnd](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.tseries.offsets.MonthEnd.html) 
* [Datetime](https://docs.python.org/3/library/datetime.html) 
* [Calendar](https://docs.python.org/3/library/calendar.html) 

### FileCompare
Compares files via set to generate a dataframe of either rows found only in left, right, both or neither. Also utilizes datacompy from Capital One to generate a row by row summary report. 
* [os](https://docs.python.org/3/library/os.html)
* [Datacompy](https://pypi.org/project/datacompy/)

### List_membership_check 
Compares files via set to generate a dataframe of either rows found only in left, right, both or neither. Also utilizes datacompy from Capital One to generate a row by row summary report. 
* [os](https://docs.python.org/3/library/os.html)
* [Datacompy](https://pypi.org/project/datacompy/)

### StringReplacement
A quick function made to scan .sas files in the current directory, look for a particular string and replacement it with another. It was created as a very simple way for legacy reports which needed to be rebranded under from one agency to another, to very simply run on all the files in one place that needed the switch made. Many team members had hundreds of files that needed the swap. This allowed automatic, very quick handling of small files.
* [os](https://docs.python.org/3/library/os.html)
* [re](https://docs.python.org/3/library/re.html)

### SubjectIDExcelConversion

Takes excel workbooks as input, one with data and IDs one with conversion IDs, converts IDs on data sheets to conversions IDs. Used for converting lab samples to subject samples or for further patient/sample obscuration in studies. Outouts data workbook with samples replaced where the orignal IDs were. 
* [os](https://docs.python.org/3/library/os.html)
* [sys](https://docs.python.org/3/library/sys.html)
* [re](https://docs.python.org/3/library/re.html)
* [xlrd](https://xlrd.readthedocs.io/en/latest/)
* [openpyxl](https://openpyxl.readthedocs.io/en/stable/)

### Character_remover_python
A little tool made to scan text files in the current directory and strip them of unwanted characters. It was made for lab members to use on the output files of WGCNA, which gives gene names in lists as "17782" which makes the user then manually remove them from every file before using in Gene ontology databases. When WGCNA outputs 70+ modules, that's 70 or more gene lists that characters need to be removed from before the files could just be straight copy and pasted into resources like DAVID. The lab I was in was manually opening each list in word, selecting all the quotation marks and replacing them with blank space. I wrote this for them in Python 2 and 3 so all they had to do was go whichever folder contained the gene lists, open the command line and specify 'python quotation_remover_python2' and it would act on all text files in the directory. Requirements:
* [os](https://docs.python.org/3/library/os.html)
* [sys](https://docs.python.org/3/library/sys.html)
