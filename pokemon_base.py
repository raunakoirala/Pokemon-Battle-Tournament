from __future__ import annotations
from bdb import effective
from random_gen import RandomGen
from typing import Type
from abc import ABC, abstractmethod
"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by ______________"



class PokemonBase(ABC):

    effectivenessTable = [1,2,0.5,1,1,0.5,1,2,1,1,2,0.5,1,1,1,1.25,1.25,1.25,2,0,1.25,1.25,1.25,0,1]
    TypeOrder = ['Fire','Grass','Water','Ghost','Normal']
    statusEffectsList = ['Burn','Poison','Paralysis','Sleep','Confusion']


    def __init__(self, hp: int, pokeType, statusEffect = '') -> None:
        '''
        Initialises the constructor for PokemonBase

        Parameters:
                hp (int): max hp of pokemon
                pokeType (string): type of pokemon
                statusEffect (String): statusEffect of pokemon
        Returns:
                None

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        '''
        self.pokeType = pokeType
                
        self.statusEffect = statusEffect

        if not (self.pokeType in ["Fire", "Grass" , "Water" , "Ghost" , "Normal"]):
            raise TypeError 
    
   
    def get_level(self):
        return self.level

    def is_fainted(self) -> bool:
        '''
        Returns the sum of two decimal numbers in binary digits.

        Returns:
                None

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        '''  
        if self.get_hp() <= 0:
            return True
        else:
            return False

    def level_up(self) -> None:
        '''
        Increases level of pokemon by 1

        Returns:
                None

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        ''' 
        self.level = self.level + 1
    @abstractmethod    
    def get_speed(self) -> int:
        "ABSTRACT METHOD"        
        pass
    @abstractmethod               
    def get_attack_damage(self) -> int:
        "ABSTRACT METHOD"  
        pass
    @abstractmethod    
    def get_defence(self) -> int:
        "ABSTRACT METHOD"  
        pass

    def lose_hp(self, lost_hp: int) -> None:
        '''
        Decreases health of pokemon using lost hp

        Parameters:
                lost_hp (int): hp lost by the pokemon

        Returns:
                None

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        '''          
        self.lost_hp += lost_hp

    def heal(self) -> None:
        '''
        Heals pokemon by setting lost hp to zero and clearing status effect

        Returns: None

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        ''' 
        self.lost_hp = 0
        self.statusEffect = ''
    @abstractmethod    
    def defend(self, damage: int) -> None:
        "ABSTRACT METHOD"
        pass

    def damage_multiplier(self, other: PokemonBase):
        effectiveMult = self.effectivenessTable[(self.TypeOrder.index(self.pokeType))*5 + (self.TypeOrder.index(other.pokeType))]
        return effectiveMult
    
    def attack(self, other: PokemonBase) -> None:
        '''
        Shows one pokemon attacking the other and status effects applied

        Parameters:
                other: Initialises other pokemon being attacked

        Returns:
                None

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        '''        
        attackTarget = other
        if self.statusEffect == 'Sleep':
            return
        if self.statusEffect == 'Confusion':
            if RandomGen.random_chance(0.5):
                attackTarget = self
        effectiveMult = self.damage_multiplier(attackTarget)
        if self.statusEffect == 'Burn':
            effectiveMult *= 0.5
            self.lose_hp(1)
        attackTarget.defend(int((self.get_attack_damage())*effectiveMult))
        if self.statusEffect == 'Poison':
            self.lose_hp(3)
        if RandomGen.random_chance(0.2):
            attackTarget.statusEffect = self.statusEffectsList[self.TypeOrder.index(self.pokeType)]
    @abstractmethod    
    def get_poke_name(self) -> str:
        "ABSTRACT METHOD"
        pass

    def __str__(self) -> str:
        '''
        Returns the pokemon details as a formatted string

        Returns:
                output (str): pokemon level, name and hp displayed

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        '''            
        output = "LV. " + str(self.level) + " "+ self.get_poke_name() + ": " + str(self.get_hp()) + " HP"
        return output

    @abstractmethod    
    def should_evolve(self) -> bool:
        "ABSTRACT METHOD"
        pass
    @abstractmethod    
    def can_evolve(self) -> bool:
        "ABSTRACT METHOD"
        pass
        
    @abstractmethod    
    def get_evolved_version(self) -> PokemonBase:
        "ABSTRACT METHOD"        
        pass

class PokeType:
    FIRE = 'fire'
    WATER = "Water"
    GHOST = "Ghost"
    GRASS = "Grass"
    NORMAL = "Normal"
