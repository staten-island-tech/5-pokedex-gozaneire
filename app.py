import json

## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")



## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
"print(data[0])"



# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
"""for i in range(809):
    print(data[i]['name']['english'])"""



# Add a language choice feature and print the pokemons name based on the user input
"""language_finnish = input('Select language:\n')

for i in data:
    print(i['name'][language_finnish])"""

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
type_input = input('Select a pokemon type\n')

for i in data:
    if type_input in i['type']:
        print(i)


# Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 



