import matplotlib.pyplot as plt
import math

def stripsales(criterion,salesdict):
	sales=open('SalesJan2009.csv','r')
	header=sales.readline().strip().split(',')
	for sale in sales:
		templist=sale.strip().split(',')
		salesdict[templist[header.index(criterion)]]=salesdict.get(templist[header.index(criterion)],0)+float(templist[header.index('Price')])
	sales.close()
	return salesdict

def add05(a):
	return a+0.25

def barchart(salesdict):
	values=list(salesdict.values())
	values.sort()
	keys=[]
	for v in values:
		for k in salesdict:
			if salesdict[k]==v:
				keys.append(k)
				salesdict.pop(k)
				break
	plt.bar(range(len(values)),values,0.5)
	plt.xticks(list(map(add05,range(len(keys)))),keys, rotation='vertical')
	plt.show()


countrysales={}
statesales={}
paymentsales={}

statesales=stripsales('State',statesales)
countrysales=stripsales('Country',countrysales)
paymentsales=stripsales('Payment_Type',paymentsales)

print(paymentsales)
barchart(countrysales)


'''
#### CREAT LISTS ####
countrylist=[]
statedict={}
topstatelist=[]
paymentlist=[]

sales=open('SalesJan2009.csv','r')
header=sales.readline().strip().split(',')
for sale in sales:
	templist=sale.strip().split(',')
	if not templist[header.index('Country')] in countrylist:
		countrylist.append(templist[header.index('Country')])
	if not templist[header.index('Payment_Type')] in paymentlist:
		paymentlist.append(templist[header.index('Payment_Type')])
	if statedict.get(templist[header.index('State')],'NA')=='NA':
		statedict[templist[header.index('State')]]=1
	else: 
		statedict[templist[header.index('State')]]=statedict.get(templist[header.index('State')],'NA')+1
sales.close()
'''