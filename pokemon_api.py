#Team Name: Kairon 07
#Team Members:
#Roswell Rey Ceniza
#Jan Michael Cabahug
#Jhun Kenneth Curacha
#Jasper Tabanag
#Jared Eli Daniot

import requests

def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url, timeout=5)
    
    if response.status_code != 200:
        raise Exception(f"Pokémon '{pokemon_name}' not found (status {response.status_code}).")
    
    data = response.json()
    return parse_pokemon_data(data)

def parse_pokemon_data(data):
    pokemon_id = data.get("id")
    name = data.get("name", "Unknown")
    types = [t["type"]["name"] for t in data.get("types", [])]
    abilities = [a["ability"]["name"] for a in data.get("abilities", [])]
    weight = data.get("weight")
    height = data.get("height")
    
    return {
        "id": pokemon_id,
        "name": name.title(),
        "types": types,
        "abilities": abilities,
        "weight": weight,
        "height": height
    }

