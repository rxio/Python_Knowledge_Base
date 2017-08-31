#A context manager automatically closes the file when you exit its code block
#It will also close the file if any exceptions or errors are thrown

with open('numbers.txt', 'r') as f:
#	f_contents = f.readlines() #returns a list of all the lines of the file
	
	for i in f:
		print(i, end='')
	
	f.seek(0) #This resets the position to read the file from the start (position 0)
	
	print() #This is a spacer
	size_to_read = 100
	f_contents = f.read(size_to_read) #reads in the first 100 characters of the file
	print(f_contents, end='')

	print() #spacer
	print(f.tell()) #This indicates what position the file is being read from

	f_contents = f.read(15) #Instead of starting over, this picks up after the last read()
	print(f_contents, end='')
	print(f.tell())

	#At the end position of the file, read returns an empty string


print(f.closed) #You can access the "f" variable outside of the context manager. However, it will be closed.
#Notice that there are no brackets after "closed".