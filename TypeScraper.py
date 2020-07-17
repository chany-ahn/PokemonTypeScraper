import urllib3
from bs4 import BeautifulSoup as bs
import requests

# url to scrape pokemone types
myUrl = 'https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number'

# Used to make the request to open page
uClient = urllib3.PoolManager()
# get the informaiton form the page
getPage = uClient.request('GET', myUrl)
# storing the html page source data
pageInfo = getPage.data

# using the beautiful soup object
soup = bs(pageInfo, 'lxml')
# maing data readable
soup.prettify()

types = ["bug", 
"dark", 
"dragon", 
"electric", 
"fairy", 
"fighting", 
"fire", 
"flying", 
"ghost", 
"grass", 
"ground", 
"ice", 
"normal", 
"poison", 
"psychic", 
"rock", 
"steel",
"water"]

pokemonList = soup.find_all('tr', style="background:#FFF")
# where index 7 holds the name 9 holds the type
monoType = []
# where index 9 and 11 hold the types
dualType = []

# place the appropriate pokemon in the appropriate list
for i in range(len(pokemonList)):
    # find all of the children of each pokemon parent node

    # if the pokemon has two types
    pokemon = pokemonList[i].contents
    if len(pokemon) == 12:
        dualType.append(pokemon)
    # if pokemon has one type
    elif len(pokemon) == 10:
        monoType.append(pokemon)

while True:
    # Take user input to see what type they want
    findType = input("What Pokemon type are you looking for? ")
    findType = findType.lower()
    if findType in types:
        break
    print("Invalid, please enter another type")

findPokemonMono = []
findPokemonDual = []

for i in range(len(monoType)):
    # find the mono-typed pokemon with desired type
    pokemonType = monoType[i][9].a.span.text
    if pokemonType.lower() == findType:
        # append the contents (for now)
        findPokemonMono.append(monoType[i])

for i in range(len(dualType)):
    # find dual-type pokemon with desired type
    pokemonType1 = dualType[i][9].a.span.text
    pokemonType2 = dualType[i][11].a.span.text
    if pokemonType1.lower() == findType or pokemonType2.lower() == findType:
        findPokemonDual.append(dualType[i])

# print out the pokemon
print("Mono-Type Pokemon")
for i in range(len(findPokemonMono)):
    print(findPokemonMono[i][7].a.text + " " + findPokemonMono[i][9].a.span.text)

print()

print("Dual-Type Pokemon")
for i in range(len(findPokemonDual)):
    print(findPokemonDual[i][7].a.text + " " + findPokemonDual[i][9].a.span.text + "/" + findPokemonDual[i][11].a.span.text)

print("Total number of " + findType + " type Pokemon is: " + str(len(findPokemonDual) + len(findPokemonMono)))