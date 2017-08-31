file = open("numbers.txt", "r") #If you don't pass in a second argument, it defaults to "r"

print(file) #This prints the file handle
print(file.name) #This prints the name of the file
print(file.mode) #This prints the mode that the file is currently in

file.close()