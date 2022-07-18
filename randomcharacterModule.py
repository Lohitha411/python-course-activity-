import  string
import random
def getRandomLowerCaseLetter():
	var1=string.ascii_letters.lower()
	chars=[]
	for i  in range(0,100):
		chars.append(random.choice(var1))
	return (chars)