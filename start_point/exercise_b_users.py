users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}



# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
print(users["Jonathan"]["twitter"])
#don't need print command for this or the other first 5

# 2. Get Erik's hometown
print(users["Erik"]["home_town"])
# correct

# 3. Get the array of Erik's lottery numbers
print(users["Erik"]["lottery_numbers"])
# correct

# 4. Get the species of Avril's pet Monty
print(users["Avril"]["pets"][0]["species"])
# correct

# 5. Get the smallest of Erik's lottery numbers
print(users["Erik"]["lottery_numbers"][2])
# sorted(users["Erik"]["lottery_numbers"])[0]

# 6. Return an array of Avril's lottery numbers that are even
print(users["Avril"]["lottery_numbers"][0], users["Avril"]["lottery_numbers"][1], users["Avril"]["lottery_numbers"][3]) #there must be a tidier way
# lottery_numbers = users["Avril"]["lottery_numbers"]
# even_numbers = []
# for lottery_number in lottery_numbers:
#     if lottery_number % 2 == 0:
#         even_numbers.append(lottery_number)

# print(even_numbers)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
users["Erik"]["lottery_numbers"] = 7 #not correct - have replaced all items with 7 rather than added
# users["Erik"]["lottery_numbers"].append(7)

# 8. Change Erik's hometown to Edinburgh
users["Erik"]["home_town"] = "Edinburgh"
#correct!

# 9. Add a pet dog to Erik called "Fluffy"
users["Erik"]["pets"] = {
  "name": "Fluffy",
  "species": "dog"
}
print(users["Erik"]["pets"]) #once again, has replaced all pets rather than adding
# users["Erik"]["pets"].append({ "name": "Fluffy", "species": "dog" })


# 10. Add another person to the users dictionary
# unsure how to add 
# users["ian"] = {
#     "twitter": "twitter name",
#     "lottery_numbers": [4,5,6,7,8],
#     "home_town": "Edinburgh",
#     "pets": [
#       {
#         "name": "Dave",
#         "species": "dog"
#       }
#     ]
# }
