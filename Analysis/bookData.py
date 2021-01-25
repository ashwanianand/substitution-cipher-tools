"""
Name : Ashwani Anand
Batch : MSC CS II
"""

import sys

data={}
letter={}

for i in range(1,23):
	name=str(i)+".txt"
	book=open("Books/"+name,"r")
	cleanBook=open("Clean/clean_"+name,"w")
	
	d=0 
	toWrite=0 
	putSpace=0
	for line in book: 
		for c in line: 
			d=ord(c) 
			if d==32 and toWrite==1: 
				toWrite=0 
				putSpace=1
			elif d>=9 and d<=13 and toWrite==1: 
				toWrite=0 
				putSpace=1
			elif d>=65 and d<=90: 
				if putSpace==1:
					cleanBook.write(" ")
				if chr(d) in letter:
					letter[chr(d)]=letter[chr(d)]+1
				else:
					letter[chr(d)]=1
				cleanBook.write(chr(d)) 
				toWrite=1 
				putSpace=0
			elif d>=97 and d<=122: 		
				if putSpace==1:
					cleanBook.write(" ")
				if chr(d-32) in letter:
					letter[chr(d-32)]=letter[chr(d-32)]+1
				else:
					letter[chr(d-32)]=1
				cleanBook.write(chr(d-32)) 
				toWrite=1 
				putSpace=0
			else: 
				continue 
	book.close()
	cleanBook.close()
	cleanBook=open("Clean/clean_"+name,"r")
	text=cleanBook.readline()
	text=text.split(' ')

	
	for word in text:
		t=len(word)
		if t==0:
			continue
		if t in data:
			if word in data[t]:
				data[t][word]=data[t][word]+1
			else:
				data[t][word]=1
		else:
			data[t]={word:1}

for len in sorted(data):
	lenFile=open(str(len)+".txt","w")
	lenFile.write("The "+str(len)+" letter words are"+chr(10)*2)
	for k in {k: v for k, v in sorted(data[len].items(), key=lambda item: item[1], reverse=True)}:
		lenFile.write(str(k)+" : "+str(data[len][k])+", ")
	lenFile.write(" ")
	lenFile.close()

letterSum=sum([y for (x,y) in letter.items()])
freqFile=open("freq.txt","w")
for k in {k: v for k, v in sorted(letter.items(), key=lambda item: item[1], reverse=True)}:
	freqFile.write(str(k)+" : "+str(round((letter[k]/letterSum)*100,3))+", ")
freqFile.close()
	
