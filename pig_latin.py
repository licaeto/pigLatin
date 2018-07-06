

"""
1.1.- Pig Latin

Nombre Alumno:Lino Cañete Tomas 

Nombre Alumno:Victor Jarilla Romo
"""

import sys


def piglatin_word(word):
	"""
	Esta función recibe una palabra en inglés y la traduce a Pig Latin
	
	:param word: la palabra que se debe pasar a Pig Latin
	:return: la palabra traducida
	"""
	voc=['a','e','i','o','u','A','E','I','O','U']

	if word[0].isnumeric():
   		return word
	else:
		if (word[0] in voc) or (word[0]=="y") or (word[0]=="Y"):
			if word.isupper():
				return word + "YAY"
			else:
				return word + "yay"
		else:
			i = 0
			while not(word[i] in voc):
				i=i+1
			if word.islower():
				return word[i:]+word[:i]+"ay"
			if word.isupper():				
				return word[i:]+word[:i]+"AY"
			if word[0].isupper():
				aux = word[0].lower()+word[1:]
				aux = aux[i:]+aux[:i]+"ay"
				aux = aux[0].upper()+aux[1:]
				return aux
				
				
					

def piglatin_sentence(sentence):
	"""
	Esta función recibe una frase en inglés i la traduce a Pig Latin

	:param sentence: la frase que se debe pasar a Pig Latin
	:return: la frase traducida
	"""
	punt=[',',';','.','?','!']
	sentence=sentence.replace(","," ,").replace(";"," ;").replace("."," .").replace("?"," ?").replace("!"," !").split(" ")
	for i in range(len(sentence)):
		if not(sentence[i] in punt):
			sentence[i]=piglatin_word(sentence[i])
	sentence=' '.join(sentence).replace(' ,',',').replace(" ;",";").replace(" .",".").replace(" ?","?").replace(" !","!")
	return sentence


if __name__ == "__main__":
	if len(sys.argv) < 2:
		while True:
			x=input('ENGLISH: ')
			if(x==""):
				break
			else:
				print("PIG LATIN: "+piglatin_sentence(x))
	if len(sys.argv) == 2:
		print (piglatin_sentence(sys.argv[1]))
		
	"""AMPLIACION"""	
	if len(sys.argv) == 3 and sys.argv[1] == "-f" : 
		f = open(sys.argv[2],"r")	
		s = open(sys.argv[2][:len(sys.argv[2])-4]+'_piglatin.txt',"w")
		c = f.read().split('\n')
		for i in range(len(c)-1):
			s.write(piglatin_sentence(c[i])+'\n')
		f.close()
	if len(sys.argv) > 3 or (len(sys.argv) == 3 and sys.argv[1] != "-f"):
		print("Argumentos incorrectos!")
