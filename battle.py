"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by ______________"

from email.base64mime import header_length
from re import A
from random_gen import RandomGen
from poke_team import Action, PokeTeam, Criterion
from print_screen import print_game_screen

class Battle:
    
    def __init__(self, verbosity=0) -> None:
        '''
        Initialises the Battle class responsible for simulating pokemon battles

        Parameters:
                    verbosity:enables printing and logging during battle
                    
        Worst case complexity: O(1)
        Best Case complexity: O(1)
        '''
        self.verbosity = verbosity 

    def battle(self, team1: PokeTeam, team2: PokeTeam) -> int:
        '''
        Responsible for simulating the battle between two teams and showing an outcome

        Parameters:
                    team1(PokeTeam): first team in battle
                    team2(PokeTeam): second team in battle

        Returns: 0, 1 or 2 depending on outcome of battle (0 = draw, 1 = player1 win, 2 = player2 win)

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        '''
        # Initialise the variables from the inputs and retrieve the first pokemon for battling
        self.team1 = team1
        self.team2 = team2
        heal1_count = 0
        heal2_count = 0
        pokemon1_on_field = team1.retrieve_pokemon()
        pokemon2_on_field = team2.retrieve_pokemon()

        while True:

            # adjusts the pokemonds speed if Paralysis status effect is applied
            player1_speed = pokemon1_on_field.get_speed()
            if pokemon1_on_field.statusEffect == 'Paralysis':
                player1_speed = player1_speed//2

            # adjusts the pokemonds speed if Paralysis status effect is applied
            player2_speed = pokemon2_on_field.get_speed()
            if pokemon2_on_field.statusEffect == 'Paralysis':
                player2_speed = player2_speed//2
            
            # gets the players actions for the turn
            player1_action = team1.choose_battle_option(pokemon1_on_field, pokemon2_on_field)
            player2_action = team2.choose_battle_option(pokemon2_on_field, pokemon1_on_field)

            # If player action is swap return the current pokeomn to the team then retrieve the next pokemon
            if player1_action == Action.SWAP:
                team1.return_pokemon(pokemon1_on_field)
                pokemon1_on_field = team1.retrieve_pokemon()
            if player2_action ==Action.SWAP:
                team2.return_pokemon(pokemon2_on_field)
                pokemon2_on_field = team2.retrieve_pokemon()

            # If player action is special perform the special operation 
            if player1_action == Action.SPECIAL:
                team1.special()
            if player2_action == Action.SPECIAL:
                team2.special()
            
            # If player action is heal then heal the pokemon
            # If the player has healed more than 3 times then the opposing team wins
            if player1_action == Action.HEAL:
                pokemon1_on_field.heal()
                heal1_count += 1
                if heal1_count > 3:
                    team1.return_pokemon(pokemon1_on_field)
                    team2.return_pokemon(pokemon2_on_field)
                    return 2      
            if player2_action == Action.HEAL:
                pokemon2_on_field.heal()
                heal2_count += 1
                if heal2_count > 3:
                    team1.return_pokemon(pokemon1_on_field)
                    team2.return_pokemon(pokemon2_on_field)                    
                    return 1
            
            # Perform the attack from player 1 to 2 
            if player1_action == Action.ATTACK and not player2_action == Action.ATTACK:
                pokemon1_on_field.attack(pokemon2_on_field)

            # Perfrom the attack from player 2 to player 1
            if player2_action == Action.ATTACK and not player1_action == Action.ATTACK:
                pokemon2_on_field.attack(pokemon1_on_field)

            # If both players attack each other check the speed of the pokemons respctively
            # Perform the attack depending on the relative speeds of the pokemon
            if player1_action == Action.ATTACK and player2_action == Action.ATTACK:
                # If pokemon 1 is faster than pokemon 2 pokemon 1 attacks first
                if player1_speed > player2_speed:
                    pokemon1_on_field.attack(pokemon2_on_field)
                    if pokemon2_on_field.is_fainted() == False:
                        pokemon2_on_field.attack(pokemon1_on_field)
                # If pokemon 2 is faster than pokemon 1 pokemon 2 attacks first
                elif player2_speed > player1_speed:
                    pokemon2_on_field.attack(pokemon1_on_field)
                    if pokemon1_on_field.is_fainted() == False:
                        pokemon1_on_field.attack(pokemon2_on_field)
                # If they have the same speed then then pokemon 1 attacks first and then pokemon 2 attacks after 
                elif player1_speed == player2_speed:
                    pokemon1_on_field.attack(pokemon2_on_field)
                    pokemon2_on_field.attack(pokemon1_on_field)
            
            # if both pokemon are still alive after the turn then both pokemon loose a health point
            if pokemon1_on_field.is_fainted() == False and pokemon2_on_field.is_fainted() == False:
                pokemon1_on_field.lose_hp(1)
                pokemon2_on_field.lose_hp(1)

            # if pokemon 1 is fainted and pokemon 2 isn't then pokemon 2 levels up and evolves if it can and pokemon 1 is returned to the team 
            if pokemon1_on_field.is_fainted() == True and pokemon2_on_field.is_fainted() == False:
                pokemon2_on_field.level_up()
                # if team 1 is empty then team 2 wins 
                if team1.is_empty() == True:
                    team2.return_pokemon(pokemon2_on_field)
                    return 2
                pokemon1_on_field = team1.retrieve_pokemon()
                if pokemon2_on_field.can_evolve() == True and pokemon2_on_field.should_evolve() == True:
                    pokemon2_on_field = pokemon2_on_field.get_evolved_version()
            
            # if pokemon 2 is fainted and pokemon 1 isn't then pokemon 1 levels up and evolves if it can and pokemon 2 is returned to the team 
            if pokemon2_on_field.is_fainted() == True and pokemon1_on_field.is_fainted() == False:
                pokemon1_on_field.level_up()
                # if team 2 is empty then team 1 wins 
                if team2.is_empty() == True:
                    team1.return_pokemon(pokemon1_on_field)
                    return 1
                pokemon2_on_field = team2.retrieve_pokemon()
                if pokemon1_on_field.can_evolve() == True and pokemon1_on_field.should_evolve() == True:
                    pokemon1_on_field = pokemon1_on_field.get_evolved_version()

            # if both pokemon are fainted check if the teams are empty and return the value for the respective winning team
            if pokemon1_on_field.is_fainted() == True and pokemon2_on_field.is_fainted() == True:
                if team1.is_empty() == True and team2.is_empty() == True:
                    return 0
                if team1.is_empty() == False and team2.is_empty() == True:
                    team1.return_pokemon(pokemon1_on_field)
                    return 1 
                if team2.is_empty() == False and team1.is_empty() == True:
                    team2.return_pokemon(pokemon2_on_field)
                    return 2
                # If none of the teams are empty retrieve the next pokemon 
                pokemon1_on_field = team1.retrieve_pokemon()
                pokemon2_on_field = team2.retrieve_pokemon()


if __name__ == "__main__":
    b = Battle(verbosity=3)
    RandomGen.set_seed(16)
    t1 = PokeTeam.random_team("Cynthia", 0, criterion=Criterion.SPD)
    t1.ai_type = PokeTeam.AI.USER_INPUT
    t2 = PokeTeam.random_team("Barry", 1)
    print(b.battle(t1, t2))
