#!/usr/bin/env python

##Run this file in terminal. The command is:  python3 common_genes.py genelist1.txt genelist2.txt

#import the data
import sys, os
import pandas as pd
inFile1=sys.argv[1]
inFile2=sys.argv[2]

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
inFile1t= os.path.join(THIS_FOLDER, inFile1)
inFile2t= os.path.join(THIS_FOLDER, inFile2)

with open(inFile1t,"r") as f:
    lista = f.readlines()
lista = [x.strip() for x in lista]
splitlist1=[]
for i in lista:
    splitlist1 += i.split(" ")


with open(inFile2t,"r") as f:
    listb = f.readlines()
listb = [x.strip() for x in listb]
splitlist2=[]
for i in listb:
    splitlist2 += i.split(" ")

nodup1 = [] 
for i in splitlist1: 
    if i not in nodup1: 
        nodup1.append(i) 
nodup2 = [] 
for i in splitlist2: 
    if i not in nodup2: 
        nodup2.append(i) 

commons = [element for element in nodup1 if element in nodup2]
num_commons = len(commons)
print(sys.argv[1] + "--" +sys.argv[2] + " common number: " + str(num_commons))
#print(commons)
#print(num_commons )

