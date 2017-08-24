key = 5

file = open("encoded.txt", "r")

for i in file:
	decode = chr(ord(i.rstrip()) - key)
	print(decode)

file.close()