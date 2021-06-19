#! /usr/bin/env python

# import python modules
from datetime import datetime
import itertools
import subprocess
import shlex
import glob

# define a function (runsteps) 
# we will use this function multiple times
def runsteps(targetfile):
    filename = targetfile.split('.')[0] # split file by '.'
    print(filename);
    snpfile = filename + '.snplist.txt';
    print(snpfile);
    #argument1 = targetfile + ">" + snpfile;
    #run linux cmd
    open (snpfile, "w")
    subprocess.call(["cut", "-f3", targetfile], stdout=snpfile);	

    sumstatsfile = filename + '.sumstats.add.avinput.txt';
    print(sumstatsfile);
    argument2 = './convert2annovar.pl -format rsid ' + snpfile + ' -dbsnpfile humandb/hg19_snp138.txt ';
    print(argument2);
    args1 = shlex.split(argument2)
    print(args1);
    #run perl script
    open (sumstatsfile, "w")
    p = subprocess.Popen(args1, stdout=sumstatsfile)
	
    argument3 = './table_annovar.pl ' + sumstatsfile + '  humandb/ -buildver hg19 -out ' + filename + ' -remove -protocol refGene,cytoBand,exac03,avsnp147,dbnsfp30a -operation gx,r,f,f,f -nastring . -csvout -polish -xref example/gene_xref.txt';
    print(argument3);
    args2 = shlex.split(argument3)
    print(args2);
    #run perl script
    p = subprocess.Popen(args2, stdout=subprocess.PIPE)
	
    return  #

def filesearch(ext):
    "Returns files with an extension"
    return [f for f in glob.glob(f"*{ext}")]
	
	
# start time of the program
startTime = datetime.now()
#get all the files with extension '.sumstats.add.txt' in current folder
files = filesearch('.sumstats.add.txt');
for filename in files:
    print(filename);
for filename in files:
	runsteps(filename);
	
print(datetime.now()-startTime)
