SAS

/* Get SAS system dates and one, two, five years back for parameters later in scripts. */
data curr_dates;
dt=today();
mon=month(dt);
yr=year(dt);
if mon=1 then rep_mon=12;
else rep_mon=mon-2;
if mon>1 then rep_yr=yr;
else rep_yr=rep_yr-1;

if mon<10 then datasetdt=cats(put(rep_yr,4.),'0',put(rep_mon,1.));
else datasetdt=cats(put(rep_yr,4.),put(rep_mon,2.));

one_yr_bck=rep_yr-1;
two_yr_bck=rep_yr-2;
five_yr_bck=rep_yr-5;


call symput('rep_mon',compress(put(rep_mon,best.)));
call symput('rep_yr',compress(put(rep_yr,best.)));
call symput('datasetdt',compress(put(datasetdt,6.)));
call symput('one_yr_bck',compress(put(one_yr_bck,best.)));
call symput('two_yr_bck',compress(put(two_yr_bck,best.)));
call symput('five_yr_bck',compress(put(five_yr_bck,best.)));
run;
%put &rep_mon &rep_yr &datasetdt &one_yr_bck &two_yr_bck &five_yr_bck;


/*In a library with datasets that all start with the same naming convention, list all of them using indsname. Then check and see if it's the most recent available data and drop it if it's not.  */

data mm_enctr_lvl;
set mylibname.datasetsstartwith_: indsname=_tablelabel_;
dtcreated=substr(_tablelabel_,length(_tablelabel_)-5,length(_tablelabel_)-1);
if dtcreated ~= &datasetdt then delete;
run;

/*YTD MACRO CALCULATOR
Basic syntax for how to take an input dataset with columns, location year, month, date and value and return a ytd value. Appends each subsequent location's dataset to a final dataset.
Final dataset is named according to the name of the input dataset
*/

%MACRO YTD_VALUES_CALC(mydata,Area);

  DATA DATA_YTD(KEEP=  Location  Year Month Date Value	YTD_Value);
       LENGTH 
              Location    $30.
			  Year          8.
			  Month         8.
			  Date          5.;


       SET &mydata(WHERE=(UPCASE(Location) = "&Area"))   ;
       BY Location Year Month Date;


	   

	   RETAIN YTD_Mon YTD_Value  0;

	   IF FIRST.YEAR THEN DO;
	     YTD_Mon  = 0;
	     YTD_Value  = 0;
	   END;

	   IF (Value GE 0) THEN DO;
	     YTD_Value + Value;
	     YTD_Mon + 1;
	   END;
	   
	   Prespective = 'YTD';
   

  RUN;

  PROC APPEND BASE=&mydata._YTD DATA=DATA_YTD FORCE NOWARN;
  RUN;

  PROC DATASETS LIBRARY=WORK NOPRINT;
       DELETE DATA_YTD;
  RUN;

%MEND YTD_VALUES_CALC;