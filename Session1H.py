# Dictionary | Multi Value Container
# key/value pair
# keys are always strings and values are any type :)

restaurant1 = {
    "title": "Shakti Om Vegetarian",
    "time_to_deliver": 41,
    "rating": 3.85
}

# we can modify data in dictionary
# restaurant1["time_to_deliver"] = 14

restaurant2 = {
    "title": "Table By Basant",
    "time_to_deliver": 35,
    "rating": 4.5
}

restaurant3 = {
    "title": "NIC Ice Cream",
    "time_to_deliver": 12,
    "rating": 4.2
}

restaurant4 = {
    "title": "Johns Pizza",
    "time_to_deliver": 15,
    "rating": 4.25
}

restaurant5 = {
    "title": "Fionnas Chinese",
    "time_to_deliver": 30,
    "rating": 3.5
}

# print(restaurant1, type(restaurant1))
# print(restaurant2, type(restaurant1))
# print(restaurant3, type(restaurant1))
# print(restaurant4, type(restaurant1))
# print(restaurant5, type(restaurant1))

# Tuple of Dictionaries
# restaurants = (restaurant1, restaurant2, restaurant3, restaurant4, restaurant5)
#               0              1            2           3             4
restaurants = restaurant1, restaurant2, restaurant3, restaurant4, restaurant5
print(restaurants)

# print(restaurants[2])

# Iterations or Loops

# while loop we need to maintain index
"""
idx = 0
while idx < len(restaurants):
    # print(restaurants[idx])
    print("-----------------------")
    print(restaurants[idx]["title"])
    print(restaurants[idx]["time_to_deliver"])
    print(restaurants[idx]["rating"])
    print("-----------------------")
    print()
    idx += 1
"""

# for loop we need not to maintain index
"""
for idx in range(0, len(restaurants)):

    # filter for time_to_deliver less than 15
    if restaurants[idx]["time_to_deliver"] <= 15:
        print("-----------------------")
        print(restaurants[idx]["title"])
        print(restaurants[idx]["time_to_deliver"])
        print(restaurants[idx]["rating"])
        print("-----------------------")
        print()
"""

# For Each Loop or Enhanced For Loop
for restaurant in restaurants:
    # print(restaurant)
    print("-----------------------")
    print(restaurant["title"])
    print(restaurant["time_to_deliver"])
    print(restaurant["rating"])
    print("-----------------------")
    print()

"""

    assignment:
    
    create tuple of dictionaries for COVID Data 
    
    maharashtra_cases = {
			"active": 72383,
			"confirmed": 1883365,
			"deaths": 48269,
			"deltaconfirmed": 2949,
			"deltadeaths": 60,
			"deltarecovered": 4610,
			"lastupdatedtime": "14/12/2020 21:13:15",
			"migratedother": 1098,
			"recovered": 1761615,
			"state": "Maharashtra",
			"statecode": "MH",
			"statenotes": ""
		}
		
	1. Iterate using loops :)
	Reference Link: https://api.covid19india.org/data.json
	
	2. Show the State with max active cases
	3. Show the State with min active cases
"""

