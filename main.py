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

    'Waterloo & City': ['Waterloo', 'Bank'],

    'DLR': [],

    'London Overground': []}

line_types = {'direct': ['Bakerloo', 'Victoria', 'Circle', 'Hammersmith & City', 'Jubilee', 'Waterloo & City'], 'divergent': ['Central', 'District', 'Metropolitan', 'Nothern', 'Piccadilly', 'DLR']}



# dictionary = {'station':['lines1', 'lines2]}
def update_connections():
    unique_stations = []
    connection_dic = {}
    for lines in trainlines:
        for stations in range(len(trainlines[lines])):
            if trainlines[lines][stations] not in unique_stations:
                unique_stations.append(trainlines[lines][stations])
                connection_dic[trainlines[lines][stations]] = []
                # print(trainlines[lines][stations])
    for linesx in trainlines:
        for x in range(len(trainlines[linesx])):
            for linesy in trainlines:
                for y in range(len(trainlines[linesy])):
                    if trainlines[linesx][x] == trainlines[linesy][y]:  # If the train stations are the same
                        if trainlines[linesx] == trainlines[linesy]:
                            break
                        elif trainlines[linesx] != trainlines[linesy]:    # But the lines are not the same.
                            # The below could be summarised into 3 lines...
                            if trainlines[linesx][x] not in connection_dic[trainlines[linesx][x]]:  # if train station is not in dictionary keys list.
                                if linesx not in connection_dic[trainlines[linesx][x]]:
                                    connection_dic[trainlines[linesx][x]].append(linesx)  # put this line_x into the dictionary station key
                                if linesy not in connection_dic[trainlines[linesx][x]]:
                                    connection_dic[trainlines[linesx][x]].append(linesy)  # put this line_y into the dictionary station key
                            if trainlines[linesx][x] in connection_dic[trainlines[linesx][x]]:
                                if linesx not in connection_dic[trainlines[linesx][x]]:
                                    connection_dic[trainlines[linesx][x]].append(linesx)
                                if linesy not in connection_dic[trainlines[linesx][x]]:
                                    connection_dic[trainlines[linesx][x]].append(linesy)
    print(connection_dic)
update_connections()
print('Updated TfL Train Map Connections. Maki Inc.')


def search(station):
    global found
    search.confirmed = False
    selected_stations = []
    for lines in trainlines:
        for x in range(len(trainlines[lines])):
            if trainlines[lines][x] == station.title():
                found = True
                search.confirmed = True
                return search.confirmed

            if trainlines[lines][x][:2] == station[:2]:
                if trainlines[lines][x] not in selected_stations:
                        selected_stations.append(trainlines[lines][x])
    if len(selected_stations) > 1:
        print('Did you mean anyone of these?? ')
        print("Please copy and paste one of these station(s) into Enter input!")
        for x in selected_stations:
            print(f'--> {x}')
        search.confirmed = True
        return search.confirmed

    else:
        print("Please make sure you type an train station with some accuracy. ")
        search.confirmed = False
        return search.confirmed


def linefinder(s_train, d_train):
    common_line = []
    s_line, d_line = ([], [])
    for lines in trainlines:
        for x in range(len(trainlines[lines])):
            if s_train in trainlines[lines][x]:
                s_line.append(lines)
            if d_train in trainlines[lines][x]:
                d_line.append(lines)
    print(f'Source Train is on {s_line}, Destination Train is on {d_line}.')
    # print("Checking if stations have a line in common...")
    for line in s_line:
        if line in d_line:
            if line not in common_line:
                common_line.append(line)
    for line in d_line:
        if line in s_line:
            if line not in common_line:
                common_line.append(line)
    if len(common_line) < 1:
        print("No lines in common found.")
    else:
        print(f"Lines found in common include: {common_line}")


while input != 'Exit':
    search.confirmed = False
    found = False
    print('Enter exit in any way to exit program...')
    while not search.confirmed:
        source_train = input('Search START train station:: ').title().strip()
        search(source_train)
        if not found and search.confirmed:
            source_train = input('Enter START train station:: ').title().strip()
    os.system('cls')
    found = False
    search.confirmed = False
    while not search.confirmed:
        dest_train = input('Search END train station:: ').title().strip()
        search(dest_train)
        if not found and search.confirmed:
            dest_train = input('Enter END train station:: ').title().strip()
    os.system('cls')
    print(f'Finding directions from {source_train} --> {dest_train}...')
    linefinder(source_train, dest_train)
    sleep(1)

# TBC
