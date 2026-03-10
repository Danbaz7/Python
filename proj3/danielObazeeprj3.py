# INF360 - Programming in Python

# Assignment 3


# ---------------------------------------------------------
# Step 1: Create a dictionary for each vehicle
# ---------------------------------------------------------

ka = {
    "name": "Ka",
    "year_introduced": 1996,
    "production_current_model": 2014,
    "generation": "3rd",
    "vehicle_information": "Developed by Ford Brazil as a super mini car"
}

fiesta = {
    "name": "Fiesta",
    "year_introduced": 1976,
    "production_current_model": 2017,
    "generation": "7th",
    "vehicle_information": "Ford's long running subcompact line based on global B-car Platform"
}

focus = {
    "name": "Focus",
    "year_introduced": 1998,
    "production_current_model": 2018,
    "generation": "3rd",
    "vehicle_information": "Ford's Compact car based on global C-car platform"
}

mondeo = {
    "name": "Mondeo",
    "year_introduced": 1992,
    "production_current_model": 2012,
    "generation": "2nd",
    "vehicle_information": "Mid sized passenger sedan with 'One-Ford' design based on CD4 platform"
}

fusion = {
    "name": "Fusion",
    "year_introduced": 2005,
    "production_current_model": 2014,
    "generation": "5th",
    "vehicle_information": "Similar to Mondeo"
}

taurus = {
    "name": "Taurus",
    "year_introduced": 1986,
    "production_current_model": 2009,
    "generation": "6th",
    "vehicle_information": "Full sized car based on D3 platform"
}

fiesta_st = {
    "name": "Fiesta ST",
    "year_introduced": 2013,
    "production_current_model": 2013,
    "generation": "1st",
    "vehicle_information": "Fiesta's high performance factory tune"
}

focus_rs = {
    "name": "Focus RS",
    "year_introduced": 2015,
    "production_current_model": 2015,
    "generation": "1st",
    "vehicle_information": "Special high performance Focus developed by SVT"
}

mustang = {
    "name": "Mustang",
    "year_introduced": 1964,
    "production_current_model": 2014,
    "generation": "6th",
    "vehicle_information": "Ford's long running pony/muscle car"
}

gt = {
    "name": "GT",
    "year_introduced": 2004,
    "production_current_model": 2016,
    "generation": "2nd",
    "vehicle_information": "Ford's limited production super car inspired by the legendary race car GT40"
}

# List of all vehicle dictionaries
vehicles = [
    ka, fiesta, focus, mondeo, fusion,
    taurus, fiesta_st, focus_rs, mustang, gt
]

# ---------------------------------------------------------
# Step 2: Convert list → dictionary keyed by vehicle name
# ---------------------------------------------------------

def build_vehicle_dict(vehicle_list):
    
    # Takes a list of vehicle dictionaries and returns a dictionary
    # where each key is the vehicle's name and the value is the full dictionary.
    
    # return {v["name"]: v for v in vehicle_list} # Comprehension style
    
    new_dict = {}
    for v in vehicle_list:
        new_dict[v["name"]] = v
    return new_dict

vehicle_dict = build_vehicle_dict(vehicles)

# ---------------------------------------------------------
# Step 3: Return a sorted list of vehicle names
# ---------------------------------------------------------

def get_sorted_vehicle_names(vehicle_dict):
    
    # Returns a list of all vehicle names sorted alphabetically.
    
    return sorted(vehicle_dict.keys())

# ---------------------------------------------------------
# Step 4: Return dictionary of {name: year_introduced}
# ---------------------------------------------------------

def get_year_introduced_dict(vehicle_dict):
    
    # Returns a dictionary mapping each vehicle's name to its year introduced.
    
    # return {name: data["year_introduced"] for name, data in vehicle_dict.items()} # Comprehension style
    
    year_map = {}
    for name, data in vehicle_dict.items():
        year_map[name] = data["year_introduced"]
    return year_map

# ---------------------------------------------------------
# Final Output: Formatting per Requirements
# ---------------------------------------------------------

# Display alphabetical names list
print("\nVEHICLE NAMES (Alphabetical):")
sorted_names = get_sorted_vehicle_names(vehicle_dict)
for name in sorted_names:
    print(name)

# Display year mapping sorted by year
print("\nYEAR --  NAME:")
year_data = get_year_introduced_dict(vehicle_dict)
# Create a list of tuples (year, name) to sort by year .
sorting_list = []
for name, year in year_data.items():
    sorting_list.append((year, name))

# Sort chronologically by year
sorting_list.sort()

for year, name in sorting_list:
    print(f"{year} : {name}")

print(' ')