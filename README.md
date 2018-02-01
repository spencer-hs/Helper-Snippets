# 
Subject-Conversion-Excel

Takes excel workbooks as input, one with data and IDs one with conversion IDs, converts IDs on data sheets to conversions IDs. Used for converting lab samples to subject samples or for further patient/sample obscuration in studies. Outouts data workbook with samples replaced where the orignal IDs were. 




Character-stripper-tool-Python
A little tool made to scan text files in the current directory and strip them of unwanted characters. It was made for lab members to use on the output files of WGCNA, which gives gene names in lists as "17782" which makes the user then manually remove them from every file before using in Gene ontology databases. When WGCNA outputs 70+ modules, that's 70 or more gene lists that characters need to be removed from before the files could just be straight copy and pasted into resources like DAVID. The lab I was in was manually opening each list in word, selecting all the quotation marks and replacing them with blank space. I wrote this for them in Python 2 and 3 so all they had to do was go whichever folder contained the gene lists, open the command line and specify 'python quotation_remover_python2' and it would act on all text files in the directory. 
