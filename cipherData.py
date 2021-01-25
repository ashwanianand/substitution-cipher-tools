"""
Name : Ashwani Anand
Batch : MSC CS II
"""

import sys

freq=['E',12.432,'T',9.118,'A',7.937,'O',7.645,'I',7.012,'N',6.868,'H',6.315,'S',6.248,'R',5.847,'D',4.386,'L',4.05,'U',2.832,'M',2.658,'C',2.432,'W',2.369,'F',2.212,'Y',2.08,'G',2.065,'P',1.747,'B',1.543,'V',0.961,'K',0.806,'X',0.139,'J',0.133,'Q',0.103,'Z',0.061]

name="Cipher"+sys.argv[1]+".txt"
cip=open(name,"r")
text=cip.readline()
cip.close()

if sys.argv[2] =="l":
	d=0
	letter={}
	for c in text:
		d=ord(c)
		if d>=65 and d<=90: 
				if chr(d) in letter:
					letter[chr(d)]=letter[chr(d)]+1
				else:
					letter[chr(d)]=1
		else:
			continue
	letterSum=sum([y for (x,y) in letter.items()])
	sortD={k: round(((v/letterSum)*100),3) for k, v in sorted(letter.items(), key=lambda item: item[1], reverse=True)}
	print(sortD)
	
	if sys.argv[3]=="y":
		textFreqList=[]
		key="" 
		for i in sortD:
			textFreqList.append(i)
			textFreqList.append(sortD[i])
		for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			key=key+textFreqList[freq.index(l)]
		keyFile=open("Key"+sys.argv[1]+".txt",'w')
		keyFile.write(key)

elif sys.argv[2] == "w":
	text=text.split(' ')

	data={}
	for word in text:
		t=len(word)
		if t in data:
			if word in data[t]:
				data[t][word]=data[t][word]+1
			else:
				data[t][word]=1
		else:
			data[t]={word:1}

	for len in sorted(data):
		print("The",len,"letter words are")
		print({k: v for k, v in sorted(data[len].items(), key=lambda item: item[1],reverse=True)})
		print(" ")
