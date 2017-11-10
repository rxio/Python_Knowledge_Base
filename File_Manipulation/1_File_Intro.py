file = open("example.txt", "w")

for i in range (21):
	file.write(str(i) + "\n") #You have to use the str() function because you are concatenating it to the string "\n", and you can't add ints to strings. If it was just "i" alone, you wouldn't have to use str() to convert it to a string

file.close()


filein = open("example.txt", "r")

for i in filein:
	print(i.rstrip()) #The reason why I use rstrip() is because print() adds another \n to the end of the line

filein.close()
