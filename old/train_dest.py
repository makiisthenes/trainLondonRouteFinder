#tr#train_dest


import requests # Implementation of TfL API
import os
import time
from routeAlgo import routeAlgrthm
from debugger_train import debugBaker, debugCentral

tfl_api_id = '158d290e'
tfl_api_key = '6192c53aa8807df16ad4f00b76bf7b00'

trainlines = ['Bakerloo', 'Central', 'Circle', 'District', 'Hammersmith & City', 'Jubilee', 'Metropolitan', 'Nothern', 'Piccadilly', 'Victoria', 'Waterloo & City', 'DLR', 'London Overground']


bakerloo_train = ['Elephant & Castle', 'Lambeth North', 'Waterloo', 'Embankment', 'Charing Cross', 'Piccadilly Circus', 'Oxford Circus', "Regent's Park", 'Baker Street', 'Marylebone', 'Edgware Road',
'Paddington', 'Warwick Avenue', 'Maida Vale', 'Kilburn Park', "Queen's Park", 'Kensal Green', 'Willesden Junction', 'Harlesden', 'Stonebridge Park', 'Wembley Central', 'North Wembley', 'South Kenton',
'Kenton', 'Harrow & Wealdstone']

central_train = ['West Ruislip', 'Ruislip Gardens', 'South Ruislip', 'Northolt', 'Greenford', 'Perivale', 'Hanger Lane', 'Ealing Broadway', 'West Acton', 'North Acton',  'East Acton', 'White City',
"Shepherd's Bush", 'Holland Park', 'Notting Hill Gate', 'Queensway', 'Lancaster Gate', 'Marble Arch', 'Bond Street', 'Oxford Circus', 'Tottenham Court Road', 'Holborn', 'Chancery Lane', "St. Paul's",
 'Bank', 'Liverpool Street', 'Bethnal Green', 'Mile End', 'Stratford', 'Leyton', 'Leytonstone', 'Wanstead', 'Redbridge', 'Gants Hill', 'Newbury Park', 'Barkingside', 'Fairlop', 'Hainault', 'Grange Hill',
  'Chigwell', 'Roding Valley', 'Snaresbrook', 'South Woodford', 'Woodford', 'Buckhurst Hill', 'Loughton', 'Debden', 'Theydon Bois', 'Epping']

circle_train = ['Hammersmith', 'Goldhawk Road', "Shepherd's Bush Market", 'Wood Lane', 'Latimer Road', 'Ladbroke Grove', 'Westbourne Park', 'Royal Oak', 'Paddington', 'Edgware Road', 'Baker Street',
 'Great Portland Street', 'Euston Square', "King's Cross St Pancras", 'Farringdon', 'Barbican', 'Moorgate', 'Liverpool Street', 'Aldgate', 'Tower Hill', 'Monument',  'Cannon Street', 'Mansion House',
  'Blackfriars', 'Temple', 'Embankment', 'Westminster', "St James's Park", 'Victoria', 'Sloane Square', 'South Kensington', 'Gloucester Road', 'High Street Kensington', 'Notting Hill Gate', 'Bayswater']


# DISTRICT LINE LIST IS GOING TO HAVE TO BE MODIFIED AND GIVEN EXACT ROUTES, AS ITS NOT POSSIBLE TO GO CERTAIN ROUTES....
district_train = ['Richmond', 'Kew Gardens', 'Gunnersbury', 'Ealing Broadway', 'Ealing Common', 'Acton Town', 'Chiswick Park', 'Turnham Green', 'Stamford Brook', 'Ravenscourt Park', 'Hammersmith',
'Barons Court', 'West Kensington', 'Wimbledon', 'Wimbledon Park', 'Southfields', 'East Putney', 'Putney Bridge', 'Parsons Green', 'Fulham Broadway', 'West Brompton', 'Kensington', 'Earls Court',
'High Street Kesington', 'Notting Hill Gate', 'Bayswater', 'Paddington', 'Edgware Road', 'Gloucester Road', 'South Kensington', 'Sloane Square', 'Victoria', 'St James Park', 'Westminster', 'Embankment',
 'Temple', 'Blackfriars', 'Mansion House', 'Canon Street', 'Monument', 'Tower Hill', 'Aldgate East', 'Whitechapel', 'Stepney Green', 'Mile End', 'Bow Road', 'Bromley-by-Bow', 'West Ham', 'Plaistow',
  'Upton Park', 'East Ham', 'Barking', 'Upney', 'Becontree', 'Dagenham', 'Dagenham East', 'Elm Park', 'Hornchurch', 'Upminster Bridge', 'Upminster']

hammer_city_train = ['Hammersmith', 'Goldhawk Road', 'Shepherds Bush Market', 'Wood Lane', 'Latimer Road', 'Ladbroke Grove', 'Westbourne Park', 'Royal Oak', 'Paddington', 'Edgware Road', 'Baker Street',
 'Great Portland Street', 'Euston Square', "King's Cross St Pancras", 'Farringdon', 'Barbican', 'Moorgate', 'Liverpool Street', 'Aldgate East', 'Whitechapel', 'Stepney Green', 'Mile End', 'Bow Road',
  'Bromley-by-Bow', 'West Ham', 'Plaistow', 'Upton Park', 'East Ham', 'Barking']

jubilee_train = ['Stanmore', "Canon's Park", "Queensbury", "Kingsbury", "Wembley Park", "Neasden", "Dollis Hill", "Willesden Green", "Kilburn", "West Hampstead", 'Finchley Road', 'Swiss Road',
 "St John's Wood", "Baker Street", "Bond Street", "Green Park", "Westminster", "Waterloo", "Southwark", "London Bridge", "Bermondsey", "Canada Water", 'Canary Wharf', "North Greenwich", "Canning Town", "West Ham", "Stratford"]

met_train = ['Aldgate', 'Liverpool Street', 'Moorgate', 'Barbican', 'Farringdon', "King's Cross St Pancras", 'Euston Square', 'Great Portland Street', 'Baker Street', 'Finchley Road', 'Wembley Park', 'Preston Road', 'Northwick Park',
 'Harrow-on-the-Hill', 'West Harrow', 'Rayners Lane', 'Eastcote', 'Ruislip Manor', 'Ruislip', 'Ickenham', 'Hillingdon', 'Uxbridge', 'North Harrow', 'Pinner', 'Northwood Hills', 'Northwood', 'Moor Park', 'Croxley', 'Watford',
  'Rickmansworth', 'Chorleywood', 'Chalfont & Latimer', 'Chesman', 'Amersham']

nothern_train = ['High Barnet', 'Totteridge & Wherstone', 'Woodside Park', 'West Finchley', 'Mill Hill East', 'Finchley Central', 'East Finchley', 'Highgate', 'Archway', 'Tufnell Park', 'Kentish Town', 'Camdem Town', 'Edgware',
 'Burnt Oak', 'Colindale', 'Hendon Central', 'Brent Cross', 'Golders Green', 'Hampstead', 'Belsize Park', 'Chalk Farm', 'Mornington Crescent', 'Euston', "King's Cross St Pancras", 'Angel', 'Old Street', 'Moorgate', 'Bank',
  'London Bridge', 'Borough', 'Elephant & Castle', 'Warren Street', 'Goodge Street', 'Tottenham Court Road', 'Leicester Square', 'Charing Cross', 'Embankment', 'Waterloo', 'Kennington', 'Oval', 'Stockwell', 'Calpham North',
   'Calpham Common', 'Clapham South', 'Balhamn', 'Tooting Bec', 'Tooting Broadway', 'Colliers Wood', 'South Wimbledon', 'Morden']

picca_train = ['Cockfosters', 'Oakwood', 'Southgate', 'Arnos Grove', 'Bounds Green', 'Wood Green', 'Turnpike Lane', 'Manor House', 'Finsbury Park', 'Arsenal', 'Holloway Road', 'Caledonian Road', "King's Cross St. Pancras",
 'Russell Square', 'Holborn', 'Covent Garden', 'Leicester Square', 'Piccadilly Circus', 'Green Park', 'Hyde Park Corner', 'Knightsbridge', 'South Kensington', 'Gloucester Road', "Earl's Court", 'Barons Court', 'Hammersmith',
  'Turnham Green', 'Acton Town', 'South Ealing', 'Northfields', 'Boston Manor', 'Osterley', 'Hounslow East', 'Hounslow Central', 'Hounslow West', 'Hatton Cross', 'Heathrow Terminal 4', 'Heathrow Terminals 2 & 3',
   'Heathrow Terminal 5', 'Ealing Common', 'North Ealing', 'Park Royal', 'Alperton', 'Sudbury Town', 'Sudbury Hill', 'South Harrow', 'Rayners Lane', 'Eastcote', 'Ruislip Manor', 'Ruislip', 'Ickenham', 'Hillingdon', 'Uxbridge']

vict_train = ['Walthamstow Central', 'Blackhorse Road', 'Tottenham Hale', 'Seven Sisters', 'Finsbury Park', 'Highbury & Islington', "King's Cross St. Pancras", 'Euston', 'Warren Street', 'Oxford Circus', 'Green Park', 'Victoria', 'Pimlico', 'Vauxhall', 'Stockwell', 'Brixton']

waterloo_train = ['Waterloo', 'Bank']

dlr_train = [] # not sure

ovrground_train = []   # will be added... after algorithm works...


def clear():
	os.system('cls')


def lineCheckSource(source_train):
	bakerCheckSource(source_train)
	centralCheckSource(source_train)
	circleCheckSource(source_train)
	districtCheckSource(source_train)
	hamcityCheckSource(source_train)
	jubileeCheckSource(source_train)
	metCheckSource(source_train)
	nothernCheckSource(source_train)
	piccaCheckSource(source_train)
	victCheckSource(source_train)
	waterlooCheckSource(source_train)


def lineCheckDest(dest_train):
	bakerCheckDest(dest_train)
	centralCheckDest(dest_train)
	circleCheckDest(dest_train)
	districtCheckDest(dest_train)
	hamcityCheckDest(dest_train)
	jubileeCheckDest(dest_train)
	metCheckDest(dest_train)
	nothernCheckDest(dest_train)
	piccaCheckDest(dest_train)
	victCheckDest(dest_train)
	waterlooCheckDest(dest_train)



def bakerCheckSource(source_train):
	# PRATICAL FUNCTION
	global onbakerloo
	onbakerloo = False
	for baker_check in bakerloo_train:
		if baker_check == source_train:
			onbakerloo = True
		elif baker_check != source_train:
			pass
	

def centralCheckSource(source_train):
	# PRATICAL FUNCTION
	global oncentral
	oncentral = False
	for central_check in central_train:
		if central_check == source_train:
			oncentral = True
		elif central_check != source_train:
			pass


def circleCheckSource(source_train):
	# PRATICAL FUNCTION
	global oncircle
	oncircle = False
	for circle_check in circle_train:
		if circle_check == source_train:
			oncircle = True
		elif circle_check != source_train:
			pass


def districtCheckSource(source_train):
	# PRATICAL FUNCTION
	global ondistrict
	oncircle = False
	for district_check in district_train:
		if district_check == source_train:
			ondistrict = True
		elif district_check != source_train:
			pass


def hamcityCheckSource(source_train):
	# PRATICAL FUNCTION
	global onhamcity
	onhamcity = False
	for hamcity_check in hammer_city_train:
		if hamcity_check == source_train:
			onhamcity = True
		elif hamcity_check != source_train:
			pass


def jubileeCheckSource(source_train):
	# PRATICAL FUNCTION
	global onjubilee
	onjubilee = False
	for jubilee_check in jubilee_train:
		if jubilee_check == source_train:
			onjubilee = True
		elif jubilee_check != source_train:
			pass


def metCheckSource(source_train):
	# PRATICAL FUNCTION
	global onmet
	onmet = False
	for met_check in met_train:
		if met_check == source_train:
			onmet = True
		elif met_check != source_train:
			pass


def nothernCheckSource(source_train):
	# PRATICAL FUNCTION
	global onnothern
	onnothern = False
	for nothern_check in nothern_train:
		if nothern_check == source_train:
			onnothern = True
		elif nothern_check != source_train:
			pass


def piccaCheckSource(source_train):
	# PRATICAL FUNCTION
	global onpicca
	onpicca = False
	for picca_check in picca_train:
		if picca_check == source_train:
			onpicca = True
		elif picca_check != source_train:
			pass


def victCheckSource(source_train):
	# PRATICAL FUNCTION
	global onvict
	onvict = False
	for vict_check in vict_train:
		if vict_check == source_train:
			onvict = True
		elif vict_check != source_train:
			pass


def waterlooCheckSource(source_train):
	# PRATICAL FUNCTION
	global onwaterloo
	onwaterloo = False
	for waterloo_check in waterloo_train:
		if waterloo_check == source_train:
			onwaterloo = True
		elif waterloo_check != source_train:
			pass

#------------------------------------------------------------------------------------
def bakerCheckDest(dest_train):
	# PRATICAL FUNCTION
	global gobakerloo
	gobakerloo = False
	for baker_check in bakerloo_train:
		if baker_check == dest_train:
			gobakerloo = True
		elif baker_check != dest_train:
			pass
	

def centralCheckDest(dest_train):
	# PRATICAL FUNCTION
	global gocentral
	gocentral = False
	for central_check in central_train:
		if central_check == dest_train:
			gocentral = True
		elif central_check != dest_train:
			pass


def circleCheckDest(dest_train):
	# PRATICAL FUNCTION
	global gocircle
	gocircle = False
	for circle_check in circle_train:
		if circle_check == dest_train:
			gocircle = True
		elif circle_check != dest_train:
			pass


def districtCheckDest(dest_train):
	# PRATICAL FUNCTION
	global godistrict
	gocircle = False
	for district_check in district_train:
		if district_check == dest_train:
			godistrict = True
		elif district_check != dest_train:
			pass


def hamcityCheckDest(dest_train):
	# PRATICAL FUNCTION
	global gohamcity
	gohamcity = False
	for hamcity_check in hammer_city_train:
		if hamcity_check == dest_train:
			gohamcity = True
		elif hamcity_check != dest_train:
			pass


def jubileeCheckDest(dest_train):
	# PRATICAL FUNCTION
	global gojubilee
	gojubilee = False
	for jubilee_check in jubilee_train:
		if jubilee_check == dest_train:
			gojubilee = True
		elif jubilee_check != dest_train:
			pass


def metCheckDest(dest_train):
	# PRATICAL FUNCTION
	global gomet
	gomet = False
	for met_check in met_train:
		if met_check == dest_train:
			gomet = True
		elif met_check != dest_train:
			pass


def nothernCheckDest(dest_train):
	# PRATICAL FUNCTION
	global gonothern
	gonothern = False
	for nothern_check in nothern_train:
		if nothern_check == dest_train:
			gonothern = True
		elif nothern_check != dest_train:
			pass


def piccaCheckDest(dest_train):
	# PRATICAL FUNCTION
	global gopicca
	gopicca = False
	for picca_check in picca_train:
		if picca_check == dest_train:
			gopicca = True
		elif picca_check != dest_train:
			pass


def victCheckDest(dest_train):
	# PRATICAL FUNCTION
	global govict
	govict = False
	for vict_check in vict_train:
		if vict_check == dest_train:
			govict = True
		elif vict_check != dest_train:
			pass


def waterlooCheckDest(dest_train):
	# PRATICAL FUNCTION
	global gowaterloo
	gowaterloo = False
	for waterloo_check in waterloo_train:
		if waterloo_check == dest_train:
			gowaterloo = True
		elif waterloo_check != dest_train:
			pass								

# ------------------------------------------------------------------------------------

if __name__ == '__main__':
	pass
else:
	print('This module should be run directly, please run train_dest.py')
	exit()	


while input != 'Exit':
	print('Enter exit in any way to exit program...')
	source_train = input('Enter START train station:: ').title()
	dest_train = input('Enter END train station:: ').title()
	# First check if train stations are recognised, if not run debugger function from module...
	lineCheckSource(source_train)
	lineCheckDest(dest_train)
	routeAlgrthm(source_train, dest_train)
	time.sleep(2)
	input('Press any button to clear and reset program...')
	clear()
	
