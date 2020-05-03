from time import sleep
import os

trainlines = {
    'Bakerloo': ['Elephant & Castle', 'Lambeth North', 'Waterloo', 'Embankment', 'Charing Cross', 'Piccadilly Circus',
                 'Oxford Circus', "Regent's Park", 'Baker Street', 'Marylebone', 'Edgware Road',
                 'Paddington', 'Warwick Avenue', 'Maida Vale', 'Kilburn Park', "Queen's Park", 'Kensal Green',
                 'Willesden Junction', 'Harlesden', 'Stonebridge Park', 'Wembley Central', 'North Wembley',
                 'South Kenton',
                 'Kenton', 'Harrow & Wealdstone'],

    'Central': ['West Ruislip', 'Ruislip Gardens', 'South Ruislip', 'Northolt', 'Greenford', 'Perivale', 'Hanger Lane',
                'Ealing Broadway', 'West Acton', 'North Acton', 'East Acton', 'White City',
                "Shepherd's Bush", 'Holland Park', 'Notting Hill Gate', 'Queensway', 'Lancaster Gate', 'Marble Arch',
                'Bond Street', 'Oxford Circus', 'Tottenham Court Road', 'Holborn', 'Chancery Lane', "St. Paul's",
                'Bank', 'Liverpool Street', 'Bethnal Green', 'Mile End', 'Stratford', 'Leyton', 'Leytonstone',
                'Wanstead', 'Redbridge', 'Gants Hill', 'Newbury Park', 'Barkingside', 'Fairlop', 'Hainault',
                'Grange Hill',
                'Chigwell', 'Roding Valley', 'Snaresbrook', 'South Woodford', 'Woodford', 'Buckhurst Hill', 'Loughton',
                'Debden', 'Theydon Bois', 'Epping'],

    'Circle': ['Hammersmith', 'Goldhawk Road', "Shepherd's Bush Market", 'Wood Lane', 'Latimer Road', 'Ladbroke Grove',
               'Westbourne Park', 'Royal Oak', 'Paddington', 'Edgware Road', 'Baker Street',
               'Great Portland Street', 'Euston Square', "King's Cross St Pancras", 'Farringdon', 'Barbican',
               'Moorgate', 'Liverpool Street', 'Aldgate', 'Tower Hill', 'Monument', 'Cannon Street', 'Mansion House',
               'Blackfriars', 'Temple', 'Embankment', 'Westminster', "St James's Park", 'Victoria', 'Sloane Square',
               'South Kensington', 'Gloucester Road', 'High Street Kensington', 'Notting Hill Gate', 'Bayswater'],

    'District': ['Richmond', 'Kew Gardens', 'Gunnersbury', 'Ealing Broadway', 'Ealing Common', 'Acton Town',
                 'Chiswick Park', 'Turnham Green', 'Stamford Brook', 'Ravenscourt Park', 'Hammersmith',
                 'Barons Court', 'West Kensington', 'Wimbledon', 'Wimbledon Park', 'Southfields', 'East Putney',
                 'Putney Bridge', 'Parsons Green', 'Fulham Broadway', 'West Brompton', 'Kensington', 'Earls Court',
                 'High Street Kesington', 'Notting Hill Gate', 'Bayswater', 'Paddington', 'Edgware Road',
                 'Gloucester Road', 'South Kensington', 'Sloane Square', 'Victoria', 'St James Park', 'Westminster',
                 'Embankment',
                 'Temple', 'Blackfriars', 'Mansion House', 'Canon Street', 'Monument', 'Tower Hill', 'Aldgate East',
                 'Whitechapel', 'Stepney Green', 'Mile End', 'Bow Road', 'Bromley-by-Bow', 'West Ham', 'Plaistow',
                 'Upton Park', 'East Ham', 'Barking', 'Upney', 'Becontree', 'Dagenham', 'Dagenham East', 'Elm Park',
                 'Hornchurch', 'Upminster Bridge', 'Upminster'],

    'Hammersmith & City': ['Hammersmith', 'Goldhawk Road', 'Shepherds Bush Market', 'Wood Lane', 'Latimer Road',
                           'Ladbroke Grove', 'Westbourne Park', 'Royal Oak', 'Paddington', 'Edgware Road',
                           'Baker Street',
                           'Great Portland Street', 'Euston Square', "King's Cross St Pancras", 'Farringdon',
                           'Barbican', 'Moorgate', 'Liverpool Street', 'Aldgate East', 'Whitechapel', 'Stepney Green',
                           'Mile End', 'Bow Road',
                           'Bromley-by-Bow', 'West Ham', 'Plaistow', 'Upton Park', 'East Ham', 'Barking'],

    'Jubilee': ['Stanmore', "Canon's Park", "Queensbury", "Kingsbury", "Wembley Park", "Neasden", "Dollis Hill",
                "Willesden Green", "Kilburn", "West Hampstead", 'Finchley Road', 'Swiss Road',
                "St John's Wood", "Baker Street", "Bond Street", "Green Park", "Westminster", "Waterloo", "Southwark",
                "London Bridge", "Bermondsey", "Canada Water", 'Canary Wharf', "North Greenwich", "Canning Town",
                "West Ham", "Stratford"],

    'Metropolitan': ['Aldgate', 'Liverpool Street', 'Moorgate', 'Barbican', 'Farringdon', "King's Cross St Pancras",
                     'Euston Square', 'Great Portland Street', 'Baker Street', 'Finchley Road', 'Wembley Park',
                     'Preston Road', 'Northwick Park',
                     'Harrow-on-the-Hill', 'West Harrow', 'Rayners Lane', 'Eastcote', 'Ruislip Manor', 'Ruislip',
                     'Ickenham', 'Hillingdon', 'Uxbridge', 'North Harrow', 'Pinner', 'Northwood Hills', 'Northwood',
                     'Moor Park', 'Croxley', 'Watford',
                     'Rickmansworth', 'Chorleywood', 'Chalfont & Latimer', 'Chesman', 'Amersham'],

    'Nothern': ['High Barnet', 'Totteridge & Wherstone', 'Woodside Park', 'West Finchley', 'Mill Hill East',
                'Finchley Central', 'East Finchley', 'Highgate', 'Archway', 'Tufnell Park', 'Kentish Town',
                'Camdem Town', 'Edgware',
                'Burnt Oak', 'Colindale', 'Hendon Central', 'Brent Cross', 'Golders Green', 'Hampstead', 'Belsize Park',
                'Chalk Farm', 'Mornington Crescent', 'Euston', "King's Cross St Pancras", 'Angel', 'Old Street',
                'Moorgate', 'Bank',
                'London Bridge', 'Borough', 'Elephant & Castle', 'Warren Street', 'Goodge Street',
                'Tottenham Court Road', 'Leicester Square', 'Charing Cross', 'Embankment', 'Waterloo', 'Kennington',
                'Oval', 'Stockwell', 'Calpham North',
                'Calpham Common', 'Clapham South', 'Balhamn', 'Tooting Bec', 'Tooting Broadway', 'Colliers Wood',
                'South Wimbledon', 'Morden'],

    'Piccadilly': ['Cockfosters', 'Oakwood', 'Southgate', 'Arnos Grove', 'Bounds Green', 'Wood Green', 'Turnpike Lane',
                   'Manor House', 'Finsbury Park', 'Arsenal', 'Holloway Road', 'Caledonian Road',
                   "King's Cross St. Pancras",
                   'Russell Square', 'Holborn', 'Covent Garden', 'Leicester Square', 'Piccadilly Circus', 'Green Park',
                   'Hyde Park Corner', 'Knightsbridge', 'South Kensington', 'Gloucester Road', "Earl's Court",
                   'Barons Court', 'Hammersmith',
                   'Turnham Green', 'Acton Town', 'South Ealing', 'Northfields', 'Boston Manor', 'Osterley',
                   'Hounslow East', 'Hounslow Central', 'Hounslow West', 'Hatton Cross', 'Heathrow Terminal 4',
                   'Heathrow Terminals 2 & 3',
                   'Heathrow Terminal 5', 'Ealing Common', 'North Ealing', 'Park Royal', 'Alperton', 'Sudbury Town',
                   'Sudbury Hill', 'South Harrow', 'Rayners Lane', 'Eastcote', 'Ruislip Manor', 'Ruislip', 'Ickenham',
                   'Hillingdon', 'Uxbridge'],

    'Victoria': ['Walthamstow Central', 'Blackhorse Road', 'Tottenham Hale', 'Seven Sisters', 'Finsbury Park',
                 'Highbury & Islington', "King's Cross St. Pancras", 'Euston', 'Warren Street', 'Oxford Circus',
                 'Green Park', 'Victoria', 'Pimlico', 'Vauxhall', 'Stockwell', 'Brixton'],

    'Waterloo & City': [],

    'DLR': [],

    'London Overground': []}


def search(station):
    search.confirmed = False
    selected_stations = []
    for lines in trainlines:
        for x in range(len(trainlines[lines])):
            if trainlines[lines][x][:2] == station[:2]:
                if trainlines[lines][x] not in selected_stations:
                    selected_stations.append(trainlines[lines][x])
    if len(selected_stations) != 1:
        print('Did you mean anyone of these?? ')
        for x in selected_stations:
            print(f'--> {x}')
    else:
        search.confirmed = True


def linefinder(s_train, d_train):
    s_line, d_line = (None, None)
    for lines in trainlines:
        for x in range(len(trainlines[lines])):
            if s_train in trainlines[lines][x]:
                s_line = lines
            if d_train in trainlines[lines][x]:
                d_line = lines
    print(f'Source train is on {str(s_line)}, Destination train is on {str(d_line)}.')


while input != 'Exit':
    print('Enter exit in any way to exit program...')
    source_train = input('Search START train station:: ').title()
    search(source_train)
    source_train = input('Enter START train station:: ').title()
    os.system('cls')
    dest_train = input('Search END train station:: ').title()
    search(dest_train)
    dest_train = input('Enter END train station:: ').title()
    os.system('cls')
    print(f'Finding directions from {source_train} --> {dest_train}...')
    linefinder(source_train, dest_train)
    sleep(1)
