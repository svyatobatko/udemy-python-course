import requests

while True:
    pokemonName = input("Write name of pokemon:")
    pokemonName = pokemonName.lower()

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemonName}"
    req = requests.get(url)
    if req.status_code == 200:
        pokemon = req.json()
        print(pokemon)

        print(f"Name is\t\t{pokemon['name']}")
        print(f"Weight is\t{pokemon['weight']}")
        print("Abilities:")
        for ability in pokemon['abilities']:
            print("\t", ability['ability']['name'])
        break
    else:
        print("This pokemon is absent in database, please try another one.")
