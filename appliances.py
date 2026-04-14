import json

## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
move_pokedex = open("./moves.json", encoding="utf8")


## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
movedata = json.load(move_pokedex)
"print(data[0])"



# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
"""for i in range(809):
    print(data[i]['name']['english'])"""



# Add a language choice feature and print the pokemons name based on the user input
"""language_finnish = input('Select language:\n')

for i in data:
    print(i['name'][language_finnish])"""

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
"""type_input = input('Select a pokemon type\n')
typecount = False

for i in data:
    if type_input in i["type"]:
        print(i['name']['english'])
        typecount = True

if typecount == False:
    print("No pokemon found for this type")"""

# Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
"""namefind = False
nameinput = input("Type characters\n")

for i in data:
    if nameinput in i["name"]["english"]:
        print(i['name']['english'])
        namefind = True

if namefind == False:
    print("No pokemon was found")"""


#Based on user input, show all moves that pokemon could learn based on type. For example, if Charizard is fire/fyling, show all fire and flying moves.
sort = input("Choose an pokemon\n")

BLUE = '\033[34m'

movetype=[]
for i in data:
    if sort == i["name"]["english"]:
        for type in i["type"]:
            movetype.append(type)

print("\n")
print("Moves:")

for type in movetype:
    for move in movedata:
        if move["type"] == type:
            print(move["ename"])
