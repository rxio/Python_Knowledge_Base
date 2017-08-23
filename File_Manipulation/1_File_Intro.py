file = open("example.txt", "w")

for i in range (21):
	file.write(str(i) + "\n")

file.close()


filein = open("example.txt", "r")

for i in filein:
	print(i.rstrip())

filein.close()