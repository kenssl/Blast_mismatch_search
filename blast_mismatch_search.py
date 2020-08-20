import os, subprocess, glob

print('Welcome to sequencing data analysis, The Pocket, designed by Dr. Gilman Siu laboratory.')

#Checking the sequencing alignment XML text files in Pocket folder
pocket = os.chdir(str(os.getcwd())+('\\pocket'))
TXTFileinpocket = glob.glob('*.txt')
TotalTXTFile = sum('.txt' in f for f in TXTFileinpocket)
print('The total number of sequencing XML text files in Pocket is: ' + str(TotalTXTFile))
TXTfiledictionary = dict(enumerate(TXTFileinpocket, 1)) #Setting a dictionary for the XML text files in Pocket folder


#Searching the variants in the text files.
def variant_call():
	a = 1
	PathtoTXTfile = os.getcwd()
	inputTXTfilename = []
	while a > 0 and a <= max(TXTfiledictionary, key=int):
		inputTXTfilename = TXTfiledictionary[a]
		fo = open(str(TXTfiledictionary[a]), 'r')
		fw = open(str(TXTfiledictionary[a])[:-4] + '_variant.csv', 'a')
		line = fo.readlines()
		query_start = int(line[0])
		query_end = int(line[1])
		query_seq = list(line[2])
		subject_seq = list(line[3])
		b = 0
		while b >= 0 and b < len(query_seq):
			if query_seq[b] == subject_seq[b]:
				pass
			else:
				fw.write(str(query_start+b) + ',' + str(subject_seq[b]) + ',' + str(query_seq[b]) +'\n')
			b = b + 1
		fo.close()
		fw.close()
		a = a + 1

variant_call()
