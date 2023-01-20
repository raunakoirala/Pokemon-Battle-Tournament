from __future__ import annotations
from typing import Tuple

from poke_team import PokeTeam
from battle import Battle
from queue_adt import CircularQueue
from random_gen import RandomGen

class BattleTower:


    def __init__(self, battle = Battle()) -> None:

        """
        Instansitats the Battle tower class
        Inputs:
        battle  -  a battle object
        Returns:
        None
        Complexity:
        Best: O(1)
        Worst: O(1)
        """
        self.battle = battle
        self.opponents = None



    def set_my_team(self, team: PokeTeam) -> None:
        """
        sets the team for use in battles
        Inputs:
        team  -  a PokeTeam object
        Returns:
        None
        Complexity:
        Best: O(1)
        Worst: O(1)
        """
        self.my_team = team

    
    def generate_teams(self, n: int) -> None:
        
        """
        Generates n random poketeams and stores them within the tower object
        Inputs:
        n  - The number of teams to generate
        Returns:
        None
        Complexity:
        Best: O(n)
        Worst: O(n)
        """
        self.opponents = CircularQueue(n*2)
        for _ in range(n):
            battleMode = RandomGen.randint(0, 1)
            team = PokeTeam.random_team(f'Team {_}',battleMode)
            self.opponents.append(RandomGen.randint(2,10))
            self.opponents.append(team)


    def __iter__(self) -> None:
        """
        Returns the iterator object
        Inputs:
        None
        Returns:
        Itterator object
        Complexity:
        Best: O(1)
        Worst: O(1)
        """
        return BattleTowerIterator(self)  
        



        

class BattleTowerIterator:

    def __init__(self, tower: BattleTower()) -> None:
        """
        Saves the object that called it
        Inputs:
        None
        Returns:
        None
        Complexity:
        Best: O(1)
        Worst: O(1)
        """
        self.tower = tower

    def __iter__(self) -> None:
        """
        Allows the object to be itterated
        Inputs:
        None
        Returns:
        None
        Complexity:
        Best: O(1)
        Worst: O(1)
        """
        return self
        
    def __next__(self) -> Tuple:
        """
        Preforms one battle of the tower
        Inputs:
        None
        Returns:
        returnVal - a tuple with the result of the battle aswell as both teams involved in one battle of the tower, and the lives remaining for the opponent faced
        Complexity:
        Best: O(1)
        Worst: O(1)
        """
        if self.tower.opponents.is_empty():
            raise StopIteration
        opponnetHealth = self.tower.opponents.serve()
        opponentTeam = self.tower.opponents.serve()
        self.tower.my_team.regenerate_team()
        opponentTeam.regenerate_team()
        battleResult = self.tower.battle.battle(self.tower.my_team,opponentTeam)
        if battleResult == 2:
            raise StopIteration
        returnVal = (battleResult,self.tower.my_team,opponentTeam,opponnetHealth-1)
        if opponnetHealth > 1:
            self.tower.opponents.append(opponnetHealth-1)
            self.tower.opponents.append(opponentTeam)
        return(returnVal)

    def avoid_duplicates(self) -> None:
        """
        Removes all PokeTeams in the tower that have two of the same class of pokemon
        Inputs:
        None
        Returns:
        returnVal - a tuple with the result of the battle aswell as both teams involved in one battle of the tower, and the lives remaining for the opponent faced
        Complexity:
        Best: O(N * P) - N = number of PokeTeam objects, P = Max number of pokemon in the PokeTeam object 
        Worst: O(N * P)
        """
        for _ in range(len(self.tower.opponents)//2):
            opponentHealth = self.tower.opponents.serve()
            opponentTeam = self.tower.opponents.serve()
            cont = False
            for pokeNumber in opponentTeam.team_numbers:
                if pokeNumber > 1:
                    cont = True
                
            if cont:
                continue
            self.tower.opponents.append(opponentHealth)
            self.tower.opponents.append(opponentTeam)
            
        

    def sort_by_lives(self):
        # 1054
        raise NotImplementedError()




