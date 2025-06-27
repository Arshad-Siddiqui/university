# Question 2: Dictionaries

def map_airports(airport_list, city_list):
    print(airport_list + city_list)


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