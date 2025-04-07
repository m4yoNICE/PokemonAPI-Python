#Team Name: Kairon 07
#Team Members:
#Roswell Rey Ceniza
#Jan Michael Cabahug
#Jhun Kenneth Curacha
#Jasper Tabanag
#Jared Eli Daniot
def get_user_input():
    while True:
        name = input("Enter Pokémon name (or 'exit' to quit): ").strip()
        if name:
            if name.lower() == "exit":
                print("Goodbye!")
                exit()
            return name
        else:
            print("Input cannot be empty.")

def confirm_continue():
    choice = input("Would you like to search another Pokémon? (y/n): ").strip().lower()
    return choice == 'y'
