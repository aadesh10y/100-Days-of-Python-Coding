goats = {
    "football": "Messi",
    "Cricket": "Kohli",
    "Boxing": "Mike Tyson"
}

# football is the key and messi is value and so on in above dictionary
print(goats["football"])

goats["Tennis"] = "Federar"
print(goats)

empty_dictionary = {}


#wipe an existing dictionary

goats = {}
print(goats)

# Edit an item in dictionary

goats["Cricket"] = "Sachin"
print(goats)

# Loop through dictionary
for key in goats:
    print(key)
    print(goats[key])