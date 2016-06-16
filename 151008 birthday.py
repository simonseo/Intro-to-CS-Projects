dictionary={}

dictionaryFile=open('birthday.txt','a')
dictionaryFile.close()
dictionaryFile=open('birthday.txt','r')
for line in dictionaryFile:
	#if ',' in line:
	#	dictionary[line[:line.index(',')]]=line[line.index(',')+1:].strip()
	data=line.strip().split(',')
	dictionary[data[0]]=data[1]
dictionaryFile.close()

choice=0

def lookup():
	name=input('name: ').lower()
	print(dictionary.get(name,'Not found'))

def addd():
	name=input('name: ').lower()
	while name in list(dictionary.keys()):
		name=input('name already exists: ').lower()
	dictionary[name]=input('birthday YYYY/MM/DD: ')

def change():
	name=input('name: ').lower()
	while not(name in list(dictionary.keys())):
		name=input('name does not exist: ').lower()
	del dictionary[name]
	dictionary[name]=input('birthday YYYY/MM/DD: ')

def delete():
	name=input('name: ').lower()
	while not(name in list(dictionary.keys())):
		name=input('name does not exist: ').lower()
	del dictionary[name]

def lisst():
	print(dictionary)
	#for name in dictionary:
	#	print(name, dictionary[name])

while choice!=5:
	choice=input('1.lookup \n2.add\n3.change\n4.delete\n5.quit\n6.list\nnumber: ')
	if choice.isdigit():
		choice=int(float(choice))
		if choice==1:
			lookup()
		elif choice==2:
			addd()
		elif choice==3:
			change()
		elif choice==4:
			delete()
		elif choice==6:
			lisst()
		print()

dictionaryFile=open('birthday.txt','w')
for name in dictionary:
	dictionaryFile.write(name+','+dictionary[name]+'\n')
dictionaryFile.close()

