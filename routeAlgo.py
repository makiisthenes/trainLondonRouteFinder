def routeAlgrthm(source_train, dest_train):
	# making a number system, where an station is 1 point, and algorithm favours the trip that requires less points...
	# chop of known paths ways, these include no connection routes...

	# USE TRAIN_LOGIC.TXT AS REFRENCE....
	if onbakerloo:
		if gobakerloo:
			# bakerloo line to bakerloo line.
			if int(bakerloo_train.index(source_train)) > int(bakerloo_train.index(dest_train)):
				print('Directions:: ' + source_train + ' --> ' + dest_train + 'via '+
				bakerloo_train[0] + ' on: ' + trainlines[0])
			elif int(bakerloo_train.index(source_train)) < int(bakerloo_train.index(dest_train)):
				print('Directions:: ' + source_train + ' --> ' + dest_train + 'via '+
				bakerloo_train[-1] + ' on: ' + trainlines[0])

		elif gocentral:
				# bakerloo line to central line.
			if int(bakerloo_train.index(source_train)) > 6:  # index of oxford circus
				print('Directions:: ' + source_train + ' --> ' + bakerloo_train[6] + ' via ' + bakerloo_train[
					0] + ' on: ' + trainlines[0])
				if int(central_train.index(dest_train)) > 19:
					print('Directions:: ' + central_train[19] + ' --> ' + dest_train + ' via ' + central_train[
						-1] + 'on: ' + trainlines[1])
				elif int(central_train.index(dest_train)) == 19:
					pass
				elif int(central_train.index(dest_train)) < 19:
					print('Directions:: ' + central_train[19] + ' --> ' + dest_train + ' via ' + central_train[
						0] + 'on: ' + trainlines[1])

			elif int(bakerloo_train.index(source_train)) == 6:
				if int(central_train.index(dest_train)) > 19:
					print('Directions:: ' + central_train[19] + ' --> ' + dest_train + ' via ' + central_train[
						-1] + 'on: ' + trainlines[1])
				elif int(central_train.index(dest_train)) == 19:
					pass
				elif int(central_train.index(dest_train)) < 19:
					print('Directions:: ' + central_train[19] + ' --> ' + dest_train + ' via ' + central_train[
						0] + 'on: ' + trainlines[1])

			elif int(bakerloo_train.index(source_train)) < 6:
				print('Directions:: ' + source_train + ' --> ' + central_train[19] + ' via ' + bakerloo_train[
					-1] + ' on: ' + trainlines[0])
				if int(central_train.index(dest_train)) > 19:
					print('Directions:: ' + central_train[19] + ' --> ' + dest_train + ' via ' + central_train[
						-1] + 'on: ' + trainlines[1])
				elif int(central_train.index(dest_train)) == 19:
					pass
				elif int(central_train.index(dest_train)) < 19:
					print('Directions:: ' + central_train[19] + ' --> ' + dest_train + ' via ' + central_train[
						0] + 'on: ' + trainlines[1])

		elif gocircle:
			#bakerloo line to circle line.
			if int(bakerloo_train.index(source_train)) > 11:
				print('Directions:: '+ source_train +' --> '+ bakerloo_train[11] + ' via ' + bakerloo_train[0] + 'on: ' + trainlines[0])		
				if int(circle_train.index(dest_train)) > 3:
					print('Directions:: '+ bakerloo_train[3] +' --> '+ dest_train + ' via ' + circle_train[] + 'on: ' + trainlines[2])
				elif int(circle_train.index(dest_train)) > 3:
					print('Directions:: '+ bakerloo_train[3] +' --> '+ dest_train + ' via ' + circle_train[] + 'on: ' + trainlines[2])
				elif int(circle_train.index(dest_train)) ==3:
					pass		

			elif int(bakerloo_train.index(source_train)) < 3:
				print('Directions:: '+ source_train +' --> '+ bakerloo_train[3] + ' via ' + bakerloo_train[24] + 'on: ' + trainlines[0])		
				if int(circle_train.index(dest_train)) > 3:
					print('Directions:: '+ bakerloo_train[3] +' --> '+ dest_train + ' via ' + circle_train[] + 'on: ' + trainlines[2])
				elif int(circle_train.index(dest_train)) > 3:
					print('Directions:: '+ bakerloo_train[3] +' --> '+ dest_train + ' via ' + circle_train[] + 'on: ' + trainlines[2])
				elif int(circle_train.index(dest_train)) ==3:
					pass

			elif int(bakerloo_train.index(source_train)) > 3 and < 8:
				
				# this is where bakerloo line is in between the 2 circle stations...
				# THIS SECTION WOULD TAKE THE BAKER STREET AS FAVOURED STATION FOR TRANSFER...
				if int(circle_train.index(dest_train)) < 18 and != 10:
					print('Directions:: '+ source_train +' --> '+ bakerloo_train[8] + ' via ' + bakerloo_train[-1] + 'on: ' + trainlines[0])
					print('Directions:: '+ bakerloo_train[8] +' --> '+ dest_train + ' via ' + circle_train[0] + 'on: ' + trainlines[2])
					#Take Baker Street, circle until Hammersmith
				elif int(circle_train.index(dest_train)) == 10:
					print('Directions:: '+ source_train +' --> '+ bakerloo_train[8] + ' via ' + bakerloo_train[-1] + 'on: ' + trainlines[0])
					#Just take the train to Baker Street
				elif int(circle_train.index(dest_train)) > 31:
					print('Directions:: '+ source_train +' --> '+ bakerloo_train[8] + ' via ' + bakerloo_train[-1] + 'on: ' + trainlines[0])
					print('Directions:: '+ bakerloo_train[8] +' --> '+ dest_train + ' via ' + circle_train[26] + 'on: ' + trainlines[2])
					# Take Baker Street, and then circle towards Westminister..		

				#THIS SECTION WOULD TAKE THE EMBANKMENT AS FAVOURED STATION FOR TRANSFER...
				elif int(circle_train.index(dest_train)) >= 18:
					print('Directions:: '+ source_train +' --> '+ bakerloo_train[3] + ' via ' + bakerloo_train[0] + 'on: ' + trainlines[0])
					print('Directions:: '+ circle_train[25] +' --> '+ dest_train +  ' on: ' + trainlines[2])
					# Take the Embankment train, and then circle towards destination
				elif int(bakerloo_train.index(source_train)) == 3:
					print('Directions:: '+ source_train +' --> '+ dest_train +  ' on: ' + trainlines[2])	
					# Take Embankment Train to destination...
				elif int(bakerloo_train.index(source_train)) == 11:
					print('Directions:: '+ source_train +' --> '+ dest_train +  ' on: ' + trainlines[2])
					# Take Paddington train to destination...
				elif int(bakerloo_train.index(source_train)) == 8:
					print('Directions:: '+ source_train +' --> '+ dest_train +  ' on: ' + trainlines[2])
					# Take Baker Street train to destination... 
				elif int(bakerloo_train.index(source_train)) < 11 and > 8:
					# Take train to Baker Street and then do dest in circle...		
					# print **source_train --> bakerloo_train[8] on trainlines[0]**
					# print **bakerloo_train[8] --> dest_train on trainlines[2]**

		elif godistrict:
			#bakerloo line to district line.


		elif gohamcity:
			#bakerloo line to hamcity line.

		elif gojubilee:
			#bakerloo line to jubilee line.	

		elif gomet:
			#bakerloo line to met line.

		elif gonothern:
			#bakerloo line to nothern line.

		elif gopicca:
			#bakerloo line to picca line.

		elif govict:
			#bakerloo line to victoria line.

		elif gowaterloo:
			#bakerloo line to waterloo line.					



	if oncentral:
		if gocentral:
			#bakerloo line to central line.	
			if int(central_train.index(oncentral)) > int(central_train.index(gocentral)):
				print('Directions:: '+ oncentral + ' --> '+ gocentral + 'via ' central_train[0] + ' on: ' + trainlines[1])
			elif int(central_train.index(oncentral)) < int(central_train.index(gocentral)):
				print('Directions:: '+ oncentral + ' --> '+ gocentral + 'via ' central_train[-1] + ' on: ' + trainlines[1])
				# check if via destinations are correct and flip [0], [-1] if wrong...

		elif gobakerloo:
			#central line to bakerloo line.

		elif gocircle:
			#central line to circle line.

		elif godistrict:
			#central line to district line.

		elif gohamcity:
			#central line to hamcity line.

		elif gojubilee:
			#central line to jubilee line.	

		elif gomet:
			#central line to met line.

		elif gonothern:
			#central line to nothern line.

		elif gopicca:
			#central line to picca line.

		elif govict:
			#central line to victoria line.

		elif gowaterloo:
			#central line to waterloo line.		



	if oncircle:
		if gobakerloo:
			#circle line to bakerloo line.
		elif gocentral:
			#circle line to central line.	
		
		elif gocircle:
			#circle line to circle line.
			if int(circle_train.index(oncircle)) > int(circle_train.index(gocircle)):
				print('Directions:: '+ oncircle + ' --> '+ gocircle + 'via ' circle_train[0] + ' on: ' + trainlines[2])
			elif int(circle_train.index(oncentral)) < int(central_train.index(gocentral)):
				print('Directions:: '+ oncircle + ' --> '+ gocircle + 'via ' circle_train[-1] + ' on: ' + trainlines[2])
				# check if via destinations are correct and flip [0], [-1] if wrong...	

		elif godistrict:
			#circle line to district line.

		elif gohamcity:
			#circle line to hamcity line.

		elif gojubilee:
			#circle line to jubilee line.	

		elif gomet:
			#circle line to met line.

		elif gonothern:
			#circle line to nothern line.

		elif gopicca:
			#circle line to picca line.

		elif govict:
			#circle line to victoria line.

		elif gowaterloo:
			#circle line to waterloo line.
	


	if ondistrict:
		if gobakerloo:
			#bakerloo line to bakerloo line.

		elif gocentral:
			#bakerloo line to central line.	
		
		elif gocircle:
			#bakerloo line to circle line.

		elif godistrict:
			#bakerloo line to district line.
			
		elif gohamcity:
			#bakerloo line to hamcity line.

		elif gojubilee:
			#bakerloo line to jubilee line.	

		elif gomet:
			#bakerloo line to met line.

		elif gonothern:
			#bakerloo line to nothern line.

		elif gopicca:
			#bakerloo line to picca line.

		elif govict:
			#bakerloo line to victoria line.

		elif gowaterloo:
			#bakerloo line to waterloo line.
	


	if onhamcity:
		if gobakerloo:
			#bakerloo line to bakerloo line.
		elif gocentral:
			#bakerloo line to central line.	
		
		elif gocircle:
			#bakerloo line to circle line.

		elif godistrict:
			#bakerloo line to district line.

		elif gohamcity:
			#bakerloo line to hamcity line.

		elif gojubilee:
			#bakerloo line to jubilee line.	

		elif gomet:
			#bakerloo line to met line.

		elif gonothern:
			#bakerloo line to nothern line.

		elif gopicca:
			#bakerloo line to picca line.

		elif govict:
			#bakerloo line to victoria line.

		elif gowaterloo:
			#bakerloo line to waterloo line.
	


	if onjubilee:
		if gobakerloo:
			#bakerloo line to bakerloo line.
		elif gocentral:
			#bakerloo line to central line.	
		
		elif gocircle:
			#bakerloo line to circle line.

		elif godistrict:
			#bakerloo line to district line.

		elif gohamcity:
			#bakerloo line to hamcity line.

		elif gojubilee:
			#bakerloo line to jubilee line.	

		elif gomet:
			#bakerloo line to met line.

		elif gonothern:
			#bakerloo line to nothern line.

		elif gopicca:
			#bakerloo line to picca line.

		elif govict:
			#bakerloo line to victoria line.

		elif gowaterloo:
			#bakerloo line to waterloo line.
	


	if onmet:
		if gobakerloo:
			#bakerloo line to bakerloo line.
		elif gocentral:
			#bakerloo line to central line.	
		
		elif gocircle:
			#bakerloo line to circle line.

		elif godistrict:
			#bakerloo line to district line.

		elif gohamcity:
			#bakerloo line to hamcity line.

		elif gojubilee:
			#bakerloo line to jubilee line.	

		elif gomet:
			#bakerloo line to met line.

		elif gonothern:
			#bakerloo line to nothern line.

		elif gopicca:
			#bakerloo line to picca line.

		elif govict:
			#bakerloo line to victoria line.

		elif gowaterloo:
			#bakerloo line to waterloo line.
	


	if onnothern:
		if gobakerloo:
			#bakerloo line to bakerloo line.
		elif gocentral:
			#bakerloo line to central line.	
		
		elif gocircle:
			#bakerloo line to circle line.

		elif godistrict:
			#bakerloo line to district line.

		elif gohamcity:
			#bakerloo line to hamcity line.

		elif gojubilee:
			#bakerloo line to jubilee line.	

		elif gomet:
			#bakerloo line to met line.

		elif gonothern:
			#bakerloo line to nothern line.

		elif gopicca:
			#bakerloo line to picca line.

		elif govict:
			#bakerloo line to victoria line.

		elif gowaterloo:
			#bakerloo line to waterloo line.



	if onpicca:
		if gobakerloo:
			#bakerloo line to bakerloo line.
		elif gocentral:
			#bakerloo line to central line.	
		
		elif gocircle:
			#bakerloo line to circle line.

		elif godistrict:
			#bakerloo line to district line.

		elif gohamcity:
			#bakerloo line to hamcity line.

		elif gojubilee:
			#bakerloo line to jubilee line.	

		elif gomet:
			#bakerloo line to met line.

		elif gonothern:
			#bakerloo line to nothern line.

		elif gopicca:
			#bakerloo line to picca line.

		elif govict:
			#bakerloo line to victoria line.

		elif gowaterloo:
			#bakerloo line to waterloo line.		
	


	if onvict:
		if gobakerloo:
			#bakerloo line to bakerloo line.
		elif gocentral:
			#bakerloo line to central line.	
		
		elif gocircle:
			#bakerloo line to circle line.

		elif godistrict:
			#bakerloo line to district line.

		elif gohamcity:
			#bakerloo line to hamcity line.

		elif gojubilee:
			#bakerloo line to jubilee line.	

		elif gomet:
			#bakerloo line to met line.

		elif gonothern:
			#bakerloo line to nothern line.

		elif gopicca:
			#bakerloo line to picca line.

		elif govict:
			#bakerloo line to victoria line.

		elif gowaterloo:
			#bakerloo line to waterloo line.
	


	if onwaterloo:
		if gobakerloo:
			#bakerloo line to bakerloo line.
		elif gocentral:
			#bakerloo line to central line.	
		
		elif gocircle:
			#bakerloo line to circle line.

		elif godistrict:
			#bakerloo line to district line.

		elif gohamcity:
			#bakerloo line to hamcity line.

		elif gojubilee:
			#bakerloo line to jubilee line.	

		elif gomet:
			#bakerloo line to met line.

		elif gonothern:
			#bakerloo line to nothern line.

		elif gopicca:
			#bakerloo line to picca line.

		elif govict:
			#bakerloo line to victoria line.

		elif gowaterloo:
			#bakerloo line to waterloo line.

# Now we need conditions...


if __name__ == '__main__':
	print('This module must not be run directly, please run train_dest.py instead, thanks')
	input('...')
	exit()
else:
	pass	