def convertTemp(value, unit):
	if not(type(value)==float or type(value)==int and type(unit)==str and unit.isalpha()):
		print('Error')
		return
	if unit=='C':
		print(value*9/5+32,'F')
	elif unit=='F':
		print((value-32)*5/9, 'C')
	else:
		print('Not a temperature unit.')

ar=123
convertTemp(34,123)
convertTemp(93.2,'F')