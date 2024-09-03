from random import randint, choice

class Pokemon:

    # Initialize Pokemon with random health and attack values
    def __init__(self, name):
        self.name = name
        self.health = randint(100, 150)
        self.attack = randint(10, 20)

    # String representation of Pokemon
    def __str__(self):
        return f"{self.name} (HP: {self.health}, ATK: {self.attack})"


class Player:

    def get_pokemon_name(self):
        while True:
            name = input("Enter Pokemon name: ").strip()
            try:
                name = int(name)
                print("Pokemon name cannot be an integer")
                continue
            except:
                return name

    # Initialize player with name, empty team and custom pokemons
    def __init__(self, name):
        self.name = name
        self.pokemon = None
        self.team = []
        self.my_pokemons = []

    def choose_pokemon(self, pokemons):
        # Choose from a list of available pokemons (pokemons argument)
        print("Choose Pokemon")

        # Return if pokemon is empty
        if not pokemons:
            print("No Pokemon available")
            return

        # Iterate over pokemons and print index to get users choice in numbers
        for count, pokemon in enumerate(pokemons):
            print(f"{count + 1}: {pokemon}")

        choice = int(input("Enter choice: ").strip()) - 1

        self.pokemon = pokemons[choice]
        self.team.append(pokemons[choice])

        # Update Pokemon list to remove chosen pokemon
        pokemons.remove(pokemons[choice])

    def switch_pokemon(self):

        # Switch Pokemons by selecting a different pokemon from team    
        if not self.team:
            print("No Pokemon to switch.")
            return

        print("Select Pokemon to switch from your team : ")

        # Iterate over team of user pokemon to select  a new main pokemon
        for count, pokemon in enumerate(self.team):
            print(f"{count + 1}: {pokemon}")
        choice = int(input("Enter choice: ").strip()) - 1

        # Update main pokemon to newly selected pokemon 
        self.pokemon = self.team[choice]

    def display_pokemon(self):

        # Display main pokemon and Team of player pokemons if not None

        print(f"\nPlayer: {self.name} Pokemon\n")

        if self.pokemon:
            print(f"Main Pokemon: {self.pokemon}")
        else:
            print("No Pokemon chosen")

        print("\nTeam\n")
        
        for count, pokemon in enumerate(self.team):
            print(f"{count + 1}: {pokemon}")

    def create_pokemon(self):

        # Create new pokemon and append to players team of pokemons

        print("Create Pokémon\n")

        name = self.get_pokemon_name()

        new_pokemon = Pokemon(name)

        # Add newly created pokemon to team and my_pokemons (Pokemons Specifically created by this user)
        self.my_pokemons.append(new_pokemon)
        self.team.append(new_pokemon)
        print("Created Pokémon".format(new_pokemon))

class Opponent(Player):
# Inherit from player class 

    def __init__(self):
        # Call Players init to create an opponent object
        super().__init__("Opponent")

    # Choose a random pokemon from list of pokemons available
    def choose_pokemon(self, pokemons):

        # return if okemon is empty
        if not pokemons:
            return

        #  Select random pokemon
        self.pokemon = pokemons[randint(0, len(pokemons) - 1)]

        # Add pokemon to team
        self.team.append(self.pokemon)
        
        print(f"Opponent chose {self.pokemon.name}")
        pokemons.remove(self.pokemon)

    def create_pokemon(self):
        # Generate a name for the opponent newpokemon
        new_pokemon = Pokemon(f"Opponent Pokémon {randint(1, 100)}")
        
        # append pokemon to team
        self.my_pokemons.append(new_pokemon)
        self.team.append(new_pokemon)
        print(f"Opponent created New Pokemon: {new_pokemon.name}")

def initiate_fighting_sequence(player, opponent):
    print("\n--- Fight Begins! ---")
    while player.pokemon.health > 0 and opponent.pokemon.health > 0:
        # Player attacks
        opponent.pokemon.health -= player.pokemon.attack
        print(f"{player.pokemon.name} attacks! {opponent.pokemon.name} has {opponent.pokemon.health} HP left.")
        if opponent.pokemon.health <= 0:
            print(f"{opponent.pokemon.name} fainted!")
            break

        # Opponent attacks
        player.pokemon.health -= opponent.pokemon.attack
        print(f"{opponent.pokemon.name} attacks! {player.pokemon.name} has {player.pokemon.health} HP left.")
        if player.pokemon.health <= 0:
            print(f"{player.pokemon.name} fainted!")
            break

    print("\n--- Fight Ends! ---")

def main():
    # Create a pokemon object for every item in the list of pokemon names
    pokemons = [Pokemon(name) for name in ["Bulbasaur", "Charmander", "Squirtle", "Pikachu", "Eevee"]]

    # Create layer and opponent objects
    player = Player("User")
    opponent = Opponent()
    
    # Choose at random who plays first (player or opponent)
    turn = choice(['player', 'opponent'])

    while True:
        print("""
        Menu:
        1: Choose Pokémon 
        2: Create Pokémon
        3: Change Main Pokémon
        4: List Pokémon
        5: Initiate Fighting Sequence
        6: Exit
        """)

        # Begin game loop

        if turn == 'player':

            # If its players turn
            print("Player's Turn\n")
            player.display_pokemon()

            # Get the players choic of decisions
            user_choice = int(input("Enter choice: ").strip())


            # Call player mehod corrensponding to user input
            if user_choice == 1:
                player.choose_pokemon(pokemons)
                turn = 'opponent'
            elif user_choice == 2:
                player.create_pokemon()
                turn = 'opponent'
            elif user_choice == 3:
                player.switch_pokemon()
                turn = 'opponent'
            elif user_choice == 4:
                # Print a list of available pokemons then display players team, and main pokemon
                print(f"Available Pokémon: {', '.join([pokemon.name for pokemon in pokemons])}")
                print("Your Pokémon:")
                player.display_pokemon()
            elif user_choice == 5:
                # Initiate fighting sequence only if both player and opponent have a main pokemon
                if player.pokemon and opponent.pokemon:
                    initiate_fighting_sequence(player, opponent)
                else:
                    print("Both players must have a Pokémon to start the fight!")
            elif user_choice == 6:
                break
            else:
                print("Invalid choice")
        else:
            # Opponents turn
            print("Opponent's Turn\n")

            # Create pokemon if there are no pokemons available to choose from
            if not pokemons and not opponent.team:
                opponent.create_pokemon()
            else:
            # Choose from available pokemons otherwise
                opponent.choose_pokemon(pokemons)
            # Switch turn to player
            turn = 'player'

if __name__ == "__main__":
    main()
