"""
Name : Ashwani Anand
Batch : MSC CS II
"""

#--- Decryption file ---

import sys

keyFile=open("Key"+sys.argv[1]+".txt", "r") #open the key
key=keyFile.readline() #key is stored in key variable
keyFile.close()

def reversePerm(key):
	rev=["0"]*26
	i=65
	for l in key:
		if l!="\n":
			rev[ord(l)-65]=chr(i)
			i=i+1
	return rev

key=reversePerm(key)

cipherFile=open("Cipher"+sys.argv[1]+".txt", "r")
messageFile=open("Message"+sys.argv[1]+".txt", "w")
d=0
for line in cipherFile:
	for c in line:
		d=ord(c)
		if d>=65 and d<=90: #capital letter			
			messageFile.write(key[d-65]) #encrypt using the key
		else:
			messageFile.write(c)

messageFile.close()
cipherFile.close()
