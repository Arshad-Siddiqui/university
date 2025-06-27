# Question 2: Dictionaries

def map_airports(airport_list, city_list):
    airports = parse_airports(airport_list)
    cities = parse_cities(city_list)

    countries = set()
    for city in cities:
        countries.add(city["country"])
    print(countries)

    return 
def parse_airports(strings):
    airports = []
    for string in strings:
        arr = string.split(",")
        airports.append({
            "IATA": arr[0],
            "ICAO": arr[1],
            "name": arr[2]
        })
    return airports

def parse_cities(strings):
    cities = []
    for string in strings:
        arr = string.split(",")
        cities.append({
            "country":  arr[0],
            "city": arr[1]
    })
    return cities



# --- Testing Section Baby! ---
test_list = [
    {
        "airports": [
"LHR,EGLL,London Heathrow Airport",
"LGW,EGKK,London Gatwick Airport",
"MAN,EGCC, Manchester Airport",
"JFK,KJFK,John F. Kennedy International Airport",
"DXB,OMDB,Dubai International Airport"
],
    "cities": [
"United Kingdom,London",
"United Kingdom,Manchester",
"France,Paris",
"United Arab Emirates,Dubai"
]
    }
    ]

for test in test_list:
    map_airports(test["airports"], test["cities"])