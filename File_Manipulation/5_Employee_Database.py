#! /usr/bin/python3

filename = 'employeeDir.txt'

while True:
	command = input('Enter a command: ').lower()

	if command == 'add':
		name = input('Name: ')
		e_id = input('ID: ')
		post = input('Position: ')
		
		fileout = open(filename, 'a')
		fileout.write(name + '\n')
		fileout.write(e_id + '\n')
		fileout.write(post + '\n')
		fileout.close()
	
	elif command == 'list':
		filein = open(filename, 'r')
		
		for i in filein:
			name = i.rstrip()
			e_id = filein.readline().rstrip()
			post = filein.readline().rstrip()
			print('{}, {}, {}'.format(name, post, e_id))
		
		filein.close()

	elif command == 'search':
		e_name = input('Enter the employee\'s name: ')

		filein = open(filename, 'r')
		for i in filein:
			if i.lower().rstrip() == e_name.lower():
				name = i.rstrip()
				e_id = filein.readline().rstrip()
				post = filein.readline().rstrip()
				print('{}, {}, {}'.format(name, e_id, post))
		filein.close()

	elif command == 'idsearch':
		search_id = input('Enter the employee\'s ID: ')

		filein = open(filename, 'r')
		for i in filein:
			name = i.rstrip()
			e_id = filein.readline().rstrip()
			post = filein.readline().rstrip()
			if search_id == e_id:
				print('{}, {}, {}'.format(name,post,e_id))
		filein.close()

	elif command == 'quit':
		break