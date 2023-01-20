from __future__ import annotations

"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by ______________"

from enum import Enum, auto
from pokemon_base import PokemonBase
from random_gen import RandomGen
from sorted_list import ListItem
from array_sorted_list import ArraySortedList
from stack_adt import ArrayStack
from queue_adt import CircularQueue
from pokemon import Charmander, Bulbasaur, Squirtle, Gastly, Eevee

class Action(Enum):
    ATTACK = auto()
    SWAP = auto()
    HEAL = auto()
    SPECIAL = auto()
    
class Criterion(Enum):
    SPD = auto()
    HP = auto()
    LV = auto()
    DEF = auto()

class PokeTeam:
    max_team_size = 6
    unevolved_pokemon_types = 5
    total_pokemon_types = 10
    class AI(Enum):
        ALWAYS_ATTACK = auto()
        SWAP_ON_SUPER_EFFECTIVE = auto()
        RANDOM = auto()
        USER_INPUT = auto()

    def __init__(self, team_name: str, team_numbers: list[int], battle_mode: int, ai_type: PokeTeam.AI, criterion:Criterion=None, criterion_value=None) -> None:
        '''
        Initialises the constructor for PokeTeam class and creates the team.

        Worst case complexity: O(n^2)
        Best Case complexity: O(n^2)
        '''
        self.team_name = team_name
        self.ai_type = ai_type
        self.battle_mode = battle_mode
        self.criterion = criterion
        self.team_numbers = team_numbers
        self.team_count = sum(self.team_numbers)
        self.flipped = False
        unevolved_pokemon_list = ArraySortedList(self.unevolved_pokemon_types)
        unevolved_pokemon_list.add(ListItem(Charmander, 0))
        unevolved_pokemon_list.add(ListItem(Bulbasaur, 1))
        unevolved_pokemon_list.add(ListItem(Squirtle, 2))
        unevolved_pokemon_list.add(ListItem(Gastly, 3))
        unevolved_pokemon_list.add(ListItem(Eevee, 4))

        if self.battle_mode == 0:
            self.team = ArrayStack(self.team_count)
            for i in range(len(self.team_numbers)-1, -1, -1):
                for j in range(self.team_numbers[i]):
                    self.team.push(unevolved_pokemon_list[i].value())

        elif self.battle_mode == 1:
            self.team = CircularQueue(self.team_count)
            for i in range(len(self.team_numbers)):
                for j in range(self.team_numbers[i]):
                    self.team.append(unevolved_pokemon_list[i].value())
        elif self.battle_mode == 2:
            k = 0
            self.team = ArraySortedList(self.team_count)
            for i in range(len(self.team_numbers)):
                for j in range(self.team_numbers[i]):
                    newPokemon = unevolved_pokemon_list[i].value()
                    newPokemon.original_order = k
                    if self.criterion == Criterion.SPD:
                        criterion_num = -newPokemon.get_speed()
                    elif self.criterion == Criterion.HP:
                        criterion_num = -(newPokemon.get_hp() + newPokemon.lost_hp)
                    elif self.criterion == Criterion.DEF:
                        criterion_num = -newPokemon.get_defence()
                    elif self.criterion == Criterion.LV:
                        criterion_num = -newPokemon.level
                    self.team.add(ListItem(newPokemon,self.team_count*(self.total_pokemon_types*criterion_num-newPokemon.pokedex_order)+newPokemon.original_order))
                    k += 1

    
    @classmethod
    def random_team(cls, team_name: str, battle_mode: int, team_size: int=None, ai_mode: PokeTeam.AI=None, **kwargs):
        '''
        Responsible for creating a random team based on team size, battle mode and the ai mode.

        Parameters:
                    team_name(str): name of the pokemon team
                    battle_mode(int): number representing battle mode
                    team_size(int): number of pokemon in the team
                    ai_mode(action): the specified mode for which ai to follow

        Returns: team created

        Worst case complexity: O(n)
        Best Case complexity: O(n)
        '''
        if team_size is None:
            team_size = RandomGen.randint(cls.max_team_size // 2, cls.max_team_size)
        team_sorted_list = ArraySortedList(cls.unevolved_pokemon_types+1)
        team_sorted_list.add(ListItem(0, 0))
        team_sorted_list.add(ListItem(team_size, team_size))
        for i in range(len(team_sorted_list.array)-2):
            random_int = RandomGen.randint(0, team_size)
            team_sorted_list.add(ListItem(random_int, random_int))

        team_numbers = [0]*(len(team_sorted_list)-1)
        for i in range(len(team_numbers)):
            team_numbers[i] = team_sorted_list[i+1].value-team_sorted_list[i].value
        if ai_mode is None:
            ai_mode = cls.AI.RANDOM
        return cls(team_name, team_numbers, battle_mode, ai_mode, **kwargs)

    def return_pokemon(self, poke: PokemonBase) -> None:
        '''
        Returns a pokemon back into the team

        Parameters:
                    poke(PokemonBase): the pokemon being returned

        Returns:
                    None

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        '''
        if poke.is_fainted():
            return
        if self.battle_mode == 0:
            self.team.push(poke)
        elif self.battle_mode == 1:
            self.team.append(poke)
        elif self.battle_mode == 2:
            if self.criterion == Criterion.SPD:
                criterion_num = -(poke.get_speed())
            elif self.criterion == Criterion.HP:
                criterion_num = -(poke.get_hp() + poke.lost_hp)
            elif self.criterion == Criterion.DEF:
                criterion_num = -poke.get_defence()
            elif self.criterion == Criterion.LV:
                criterion_num = -poke.level
            self.team.add(ListItem(poke, self.team_count * (self.total_pokemon_types * criterion_num - poke.pokedex_order) + poke.original_order))

    def retrieve_pokemon(self) -> PokemonBase | None:
        '''
        Gets a pokemon from the team

        Returns:
                None, if the team is empty

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        '''
        if self.is_empty():
            return None
        if self.battle_mode == 0:
            return self.team.pop()
        elif self.battle_mode == 1:
            return self.team.serve()
        elif self.battle_mode == 2:
            return self.team.delete_at_index(self.flipped * (len(self.team)-1)).value

    def special(self) -> None:
        '''
        Completes special operation on the team

        Returns:
                None
                
        Worst case complexity: O(n)
        Best Case complexity: O(n)
        '''
        if self.battle_mode == 0 and len(self.team) > 1:
            team_length = len(self.team)
            first_poke = self.team.pop()
            if team_length > 2:
                poke_buffer = ArrayStack(team_length-1)  # Temporarily store pokemon while switching
                for i in range(team_length-2):
                    poke_buffer.push(self.team.pop())
            last_poke = self.team.pop()
            self.team.push(first_poke)
            if team_length > 2:
                for i in range(team_length-2):
                    self.team.push(poke_buffer.pop())
            self.team.push(last_poke)
        if self.battle_mode == 1 and len(self.team) > 1:
            poke_buffer = ArrayStack(len(self.team) // 2)  # Temporary storage for first half of team, stack is used to reverse order
            for i in range(len(poke_buffer.array)):
                poke_buffer.push(self.team.serve())
            for i in range(len(poke_buffer.array)):
                self.team.append(poke_buffer.pop())
        if self.battle_mode == 2:
            self.flipped = not(self.flipped)
            
    def regenerate_team(self) -> None:
        '''
        Regenerates team with pre-defined numbers as preperation for another battle

        Returns:
                None
                
        Worst case complexity: O(1)
        Best Case complexity: O(1)
        '''
        self.__init__(self.team_name, self.team_numbers, self.battle_mode, self.ai_type, self.criterion)

    def __str__(self) -> str:
        '''
        Returns and displays the team details, formatted as a string

        Worst case complexity: O(n)
        Best Case complexity: O(n)
        '''
        if self.team.is_empty():
            return f'[{self.team_name} ({self.battle_mode}): []'
        res = f'{self.team_name} ({self.battle_mode}): ['
        if self.battle_mode == 0:
            poke_buffer = ArrayStack(len(self.team)-1)
            for i in range(len(self.team)-1):
                temp_poke = self.team.pop()
                res += f'{temp_poke}, '
                poke_buffer.push(temp_poke)
            res += f'{self.team.peek()}]'
            for i in range(len(poke_buffer)):
                self.team.push(poke_buffer.pop())
        if self.battle_mode == 1:
            for i in range(len(self.team) - 1):
                temp_poke = self.team.serve()
                res += f'{temp_poke}, '
                self.team.append(temp_poke)
            temp_poke = self.team.serve()
            res += f'{temp_poke}]'
            self.team.append(temp_poke)
        if self.battle_mode == 2:
            for i in range(self.flipped*(len(self.team)-1), int(not(self.flipped)) * (len(self.team)-1), 1 + self.flipped*-2):
                res += f'{self.team[i].value}, '
            res += f'{self.team[int(not self.flipped) * (len(self.team)-1)].value}]'
        return res

    def is_empty(self) -> bool:
        '''
        Checks if the team is empty

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        '''
        return self.team.is_empty()

    def choose_battle_option(self, my_pokemon: PokemonBase, their_pokemon: PokemonBase) -> Action:
        '''
        Decides on AI actions based on pokemon battling

        Parameters:
                    my_pokemon(PokemonBase): first pokemon belonging to me on field
                    their_pokemon(PokemonBase): other pokemon on field
                    
        Returns:
                Action(Enum)
                
        Worst case complexity: O(1)
        Best Case complexity: O(1)
        '''
        if self.ai_type == self.AI.ALWAYS_ATTACK:
            return Action.ATTACK
        elif self.ai_type == self.AI.SWAP_ON_SUPER_EFFECTIVE:
            if their_pokemon.damage_multiplier(my_pokemon) >= 1.5:
                return Action.SWAP
            else:
                return Action.ATTACK
        elif self.ai_type == self.AI.RANDOM:
            return Action(RandomGen.randint(1,4))
        elif self.ai_type == self.AI.USER_INPUT:
            user_input = input("Your Move: ")
            if user_input == "A":
                return Action.ATTACK
            elif user_input == "P":
                return Action.SWAP
            elif user_input == "H":
                return Action.HEAL
            elif user_input == "S":
                return Action.SPECIAL

    @classmethod
    def leaderboard_team(cls):
        raise NotImplementedError()
