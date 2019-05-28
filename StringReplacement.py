import re
import os

folder='C:/Users/XXX/Desktop/TEST REQUESTS/'

for f in os.listdir(folder):
    #print(f)
    if f.endswith('.sas') or f.endswith('.R'):
        content=open(folder+f,'r').read()
        #print(content)
        new=re.sub('United Network For Organ Sharing','Organ Procurement and Transplantation Network', content,flags=re.IGNORECASE)
        
        with open(folder+f,'w') as z:
            z.write(new)
