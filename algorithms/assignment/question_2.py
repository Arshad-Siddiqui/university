# Question 2: Dictionaries

def map_airports(airport_list, city_list):
    """Maps airports to cities to countries.
    Parses lists of strings of airports and cities to build a nested dictionary.
    
    Args:
        airport_list (list[str]):
            "IATA,ICAO,Airport Name".
        city_list (list[str]):
            "Country,City".

    Returns:
        dict[str, dict[str, set[str]]]: A nested dictionary where the top-level 
        keys are country names, mapped to dicts of city names, which map 
        to sets of IATA codes for airports found in those cities.

    Raises:
        ValueError: If IATA or ICAO codes contain non-alphabet characters.
        ValueError: If IATA is not exactly 3 letters long.
        ValueError: If ICAO is not exactly 4 letters long.
    """
    # Creates nested dict containing countries that map to cities
    # that map to empty sets
    countries = {}
    for city in city_list:
        country, city_name = city.split(",")
        if country in countries:
            countries[country][city_name] = set()
        else:
            countries[country] = {city_name: set()}

    # Fills the empty sets with IATA codes assuming correctly formatted
    for airport in airport_list:
        iata, icao, airport_name = airport.split(",")
        if not iata.isalpha() or not icao.isalpha():
            raise ValueError("IATA and ICAO must not contain numbers or special values")
        if len(iata) != 3:    
            raise ValueError("IATA code must be 3 letters long")
        if len(icao) != 4:
            raise ValueError("ICAO code must be 4 letters long")
    
        for country, cities in countries.items():
            for city in cities:
                if city.lower() in airport_name.lower():
                    countries[country][city].add(iata)
                    break  # Found match
        
        # Deletes city keys that do not have any IATA codes
        for country, cities in countries.items():
            for city in cities:
                if len(city) == 0:
                    del cities[city]
    return countries

# --- Testing Section ---
# test_list = [
#     {
#         "description": "default case where it should just work",
#         "airports": [
# "LHR,EGLL,London Heathrow Airport",
# "LGW,EGKK,London Gatwick Airport",
# "MAN,EGCC, Manchester Airport",
# "JFK,KJFK,John F. Kennedy International Airport",
# "DXB,OMDB,Dubai International Airport"
# ],
#     "cities": [
# "United Kingdom,London",
# "United Kingdom,Manchester",
# "France,Paris",
# "United Arab Emirates,Dubai"
# ]
#     },
#     {
#         "description": "should raise error because IATA is wrong length",
#         "airports": [
# "LR,EGLL,London Heathrow Airport",
# "LGW,EGKK,London Gatwick Airport",
# "MAN,EGCC, Manchester Airport",
# "JFK,KJFK,John F. Kennedy International Airport",
# "DXB,OMDB,Dubai International Airport"
# ],
#     "cities": [
# "United Kingdom,London",
# "United Kingdom,Manchester",
# "France,Paris",
# "United Arab Emirates,Dubai"
# ]
#     }
#     ]

# for test in test_list:
#     print(test["description"])
#     print(map_airports(test["airports"], test["cities"]))