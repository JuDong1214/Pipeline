from datetime import datetime
import sys, getopt


#start time of the program
startTime = datetime.now()
print("****** start read " + sys.argv[1] + " *********")
#if sys.argv[1] != 'TraitsOutputfile.csv':
cand = open(sys.argv[1], 'r')
#else: 
	#return
#cand1 = open('TraitsOutputfile.csv', 'a')
try:
	f = open('ZTraitsOutputfile.csv')
	f.close()
	cand1 = open('ZTraitsOutputfile.csv', 'a')
except OSError:
	cand1 = open('ZTraitsOutputfile.csv', 'w')

words= []
for line in cand:
	line = line.strip('\n').split(',')
	words.append(line[6])	
	
cand1.write("****** start read " + sys.argv[1] + " *********" + '\n')
words_counted = []
for word in words:
	if word not in [row[0] for row in words_counted]:
		wordcount = words.count(word)
		words_counted.append((word,wordcount))
		print(word,wordcount)
		lineresult = word + ':' + str(wordcount)	
		cand1.write(lineresult + '\n')
print("****** end read " + sys.argv[1] + " *********\n")
cand1.write("****** end read " + sys.argv[1] + " *********" + '\n')
cand1.close()
