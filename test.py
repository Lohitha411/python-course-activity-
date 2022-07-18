import RandomCharacterModule
chars=RandomCharacterModule.getRandomLowerCaseLetter()
print('list chars with random characters')
print(chars)
counts=[]
def countX(chars,x):
	count=0
	for ele in chars:
		if(ele==x):
	   	 count=count+1
	return count
	
	
for i in range(97,123):
	counts.append(countX(chars,chr(i)))
print('counts for each character in list chars is:\n',counts)