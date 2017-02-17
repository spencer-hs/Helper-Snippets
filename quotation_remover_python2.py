import sys
import os

if len(sys.argv) <1:
    print "Usage: python %s requires input directory" % (sys.argv[0])
    sys.exit()

#dir_name=
#infile= sys.argv[1]
#outfile=infile.split(".")[0] + "_output.txt"
dirs= os.listdir('.')


##header=INFH.readline()
##header= header.strip()




for f in dirs:
  if f.endswith(".txt"):
      infile=f
      outfile=f.split(".")[0] + "_output.txt"
      INFH=open(f)
      OFH=open(outfile, "w")
      with open(f) as fh:
          for line in fh:
              line=line.replace('\"','')
              
              print >> OFH, line, \

      print "Output file=", outfile

      INFH.close()

