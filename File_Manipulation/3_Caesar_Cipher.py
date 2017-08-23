#! /usr/bin/python3

key = 5

f = open("encoded.txt", "w")

while True:
	try:
		char = input("Enter a letter: ")
	except:
		print("a")

	if len(char) != 1:
		break

	code = chr(ord(char)+key)
	print(code)

	f.write(code + "\n")

f.close()