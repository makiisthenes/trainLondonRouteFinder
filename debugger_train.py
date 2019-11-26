#debugger_train.py

def debugBaker(source_train, onbakerloo):
	# USER INTERFACE, DEBUGGING	
	if onbakerloo:
		print(source_train + ' is on the ' + trainlines[0] + ' line...')
	elif not onbakerloo:
		print('Maybe you meant one of these train stations on the '+ trainlines[0].upper() + ' LINE')
		baker_source_train_1st_lttr = source_train[0]
		bakernum = 0
		hasbakerloocontent = False
		for baker_check_1st in bakerloo_train:
			if baker_source_train_1st_lttr == baker_check_1st[0]:
				print('--> ' + "'"+ bakerloo_train[bakernum] +"'" )
				hasbakerloocontent = True
			bakernum = bakernum+1
		if not hasbakerloocontent:
			print('--> None')


def debugCentral(source_train, oncentral):	
	# USER INTERFACE, DEBUGGING
	if oncentral:
		print(source_train + ' is on the ' + trainlines[1] + ' line...')
	elif not oncentral:
		central_source_train_1st_lttr = source_train[0]
		centralnum = 0
		hascentralcontent = False
		print('Maybe you meant one of these train stations on the ' + trainlines[1].upper() + ' LINE')
		for central_check_1st in central_train:
			if central_source_train_1st_lttr == central_check_1st[0]:
				print('--> ' + "'"+ central_train[centralnum] +"'" )
				hascentralcontent = True
			centralnum = centralnum+1
		if not hascentralcontent:
			print('--> None')


def debugCircle(source_train, oncircle):	
	# USER INTERFACE, DEBUGGING
	if oncircle:
		print(source_train + ' is on the ' + trainlines[1] + ' line...')
	elif not oncircle:
		circle_source_train_1st_lttr = source_train[0]
		circlenum = 0
		hascirclecontent = False
		print('Maybe you meant one of these train stations on the ' + trainlines[2].upper() + ' LINE')
		for circle_check_1st in circle_train:
			if circle_source_train_1st_lttr == circle_check_1st[0]:
				print('--> ' + "'"+ circle_train[circlenum] +"'" )
				hascirclecontent = True
			circlenum = circlenum+1
		if not hascirclecontent:
			print('--> None')







# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	print('This module must not be run directly, please run train_dest.py instead, thanks')
	input('...')
	exit()
else:
	pass	

#print(onbakerloo)
	#print(oncentral)
	#print(oncircle)
	#print(ondistrict)
	#print(onhamcity)
	#print(onjubilee)
	#print(onmet)
	#print(onnothern)
	#print(onpicca)
	#print(onvict)
	#print(onwaterloo)	