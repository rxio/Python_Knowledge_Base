#! /usr/bin/python3

key = 5

f = open("encoded.txt", "w")

while True:
	char = input("Enter a letter: ")

	if len(char) != 1:
		break

	code = chr(ord(char)+key)
	print(code)

	f.write(code + "\n")

f.close()