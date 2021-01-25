"""
Name : Ashwani Anand
Batch : MSC CS II
"""

import sys

key=sys.argv[1]

def reversePerm(key):
	rev=["0"]*26
	i=65
	for l in key:
		if l!="\n":
			rev[ord(l)-65]=chr(i)
			i=i+1
	return rev

keyList=reversePerm(key)
k=""
for c in keyList:
	k=k+c
print(k)	
