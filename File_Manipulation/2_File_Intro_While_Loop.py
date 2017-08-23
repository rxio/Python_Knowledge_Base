fileout = open("example_2.txt", "w")

i = 0
while i <= 20:
	fileout.write(str(i) + "\n") 
	i+=1

fileout.close()



filein = open("example_2.txt", "r")

file = filein.readline()
while file != "":
	print(file.rstrip())
	file = filein.readline()

filein.close()