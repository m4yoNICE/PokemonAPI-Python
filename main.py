#Team Name: Kairon 07
#Team Members:
#Roswell Rey Ceniza
#Jan Michael Cabahug
#Jhun Kenneth Curacha
#Jasper Tabanag
#Jared Eli Daniot

from pokemon_api import get_pokemon_data
from input_feature import get_user_input, confirm_continue
from error_handling import handle_error, log_info

def display_pokemon(data):
    print("\n--- Pokémon Info ---")
    print(f"ID: {data['id']}")
    print(f"Name: {data['name']}")
    print(f"Types: {', '.join(data['types'])}")
    print(f"Abilities: {', '.join(data['abilities'])}")
    print(f"Height: {data['height']} decimetres")
    print(f"Weight: {data['weight']} hectograms")
    print("----------------------\n")

def main():
    while True:
        pokemon_name = get_user_input()
        try:
            log_info(f"Fetching data for '{pokemon_name}'")
            data = get_pokemon_data(pokemon_name)
            display_pokemon(data)
        except Exception as e:
            handle_error(e)
        
        if not confirm_continue():
            break

if __name__ == "__main__":
    main()
