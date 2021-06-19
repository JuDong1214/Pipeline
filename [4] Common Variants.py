#!/usr/bin/env python

##Run this file in terminal. The command is:  python3 common_variations.py trait1.txt trait2.txt.txt

#import the data
import sys, os
import pandas as pd
inFile1=sys.argv[1]
inFile2=sys.argv[2]
inFile1t=os.path.splitext(inFile1)[1]
inFile2t=os.path.splitext(inFile2)[1]
outFile1 = os.path.splitext(inFile1)[0]
outFile2 = os.path.splitext(inFile2)[0]

#saving the excels as pandas tables
if inFile1t=='.xls' or inFile1t=='.xlsx':
    tb1 = pd.read_excel(inFile1)
if inFile1t=='.csv':
    tb1 = pd.read_csv(inFile1)

if inFile2t=='.xls' or inFile2t=='.xlsx':
    tb2 = pd.read_excel(inFile2)
if inFile2t=='.csv':
    tb2 = pd.read_csv(inFile2)

#creating a new column with Chr + Start info
df1 = pd.DataFrame(tb1)
df1['chrstart'] = df1[['Chr', 'Start']].astype(str).apply(lambda x: ','.join(x), axis=1)
df2 = pd.DataFrame(tb2)
df2['chrstart'] = df2[['Chr', 'Start']].astype(str).apply(lambda x: ','.join(x), axis=1)

#Saving all the rows in the chrstart to a list
list1 = df1["chrstart"].tolist()
list2 = df2["chrstart"].tolist()

#comparing the two lists
#another way of doing is using set if you prefer that
#set1 = set(list1)
#commons = set1.intersection(list2)
#num_commons = set1.len()

commons = [element for element in list1 if element in list2]
num_commons = len(commons)
print(num_commons )
print(commons)
