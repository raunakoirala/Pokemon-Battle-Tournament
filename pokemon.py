"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by ______________"

# Importing the parent class to use for the individual pokemon
from pokemon_base import PokemonBase



class Charizard(PokemonBase):
    pokedex_order = 1 #ordering of pokemon party
    def __init__(self, lost_hp: int = 0, original_order: int|None = None):
        '''
        Initialises the constructor for Charizard class

        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        self.original_order = original_order
        self.lost_hp = lost_hp
        self.level = 3
        self.pokeType = "Fire"
        PokemonBase.__init__(self,self.get_hp() + self.lost_hp, self.pokeType)

    def get_speed(self) -> int:
        '''
        Gets the speed of the Charizard
        Returns: speed of Charizard based on level and pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        return 9 + self.level
    
    def get_hp(self) -> int:
        '''
        Gets the hp of the Charizard
        Returns: hp of Charizard based on level, pre-given value and lost hp
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        return 12 + self.level - self.lost_hp
    
    def get_attack_damage(self) -> int:
        '''
        Gets the attack damage of the Charizard
        Returns: attack damage of Charizard based on level and pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        return 10 + 2*self.level
    
    def get_defence(self) -> int:
        '''
        Gets the defence of the Charizard
        Returns: defence of Charizard based on pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        return 4
    
    def defend(self, damage: int) -> None:
        '''
        Charizard uses defend to reduce incoming damage when possible
        Returns: None
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        if damage > self.get_defence():
            self.lose_hp(2*damage)
        else:
            self.lose_hp(damage)
            
    def can_evolve(self) -> bool:
        '''
        Checks if Charizard has an evolved version
        Returns: False, as pokemon does'nt have evolved version
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''  
        return False
    
    def should_evolve(self) -> bool:
        '''
        Checks if Charizard is at the level of evolution
        Returns: False, as pokemon does'nt have evolved version
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''       
        return False
    
    def get_evolved_version(self):
        '''
        Gets the evolved version of the Charizard
        Returns: Exception as Charizard does not have an evolved form
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        raise Exception("Pokemon has no evolved version")
    
    def get_poke_name(self) -> str:
        '''
        Gets the name of the pokemon
        Returns: name of the pokemon as a string
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        return "Charizard"


class Charmander(PokemonBase):
    pokedex_order = 0
    def __init__(self, lost_hp: int = 0, original_order: int|None = None):
        '''
        Initialises the constructor for Charmander class

        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        self.original_order = original_order
        self.lost_hp = lost_hp
        self.level = 1
        self.pokeType = "Fire"
        PokemonBase.__init__(self,self.get_hp() + self.lost_hp, self.pokeType)

    def get_speed(self) -> int:
        '''
        Gets the speed of the Charmander
        Returns: speed of Charmander based on level and pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        return 7 + self.level
    
    def get_hp(self) -> int:
        '''
        Gets the hp of the Charmander
        Returns: hp of Charmander based on level, pre-given value and lost hp
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        return 8 + self.level - self.lost_hp
    
    def get_attack_damage(self) -> int:
        '''
        Gets the attack damage of the Charmander
        Returns: attack damage of Charmander based on level and pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        return 6 + self.level
    
    def get_defence(self) -> int:
        '''
        Gets the defence of the Charmander
        Returns: defence of Charmander based on pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        return 4
    
    def defend(self, damage: int) -> None:
        '''
        Charmander uses defend to reduce incoming damage when possible
        Returns: None
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        if damage > self.get_defence():
            self.lose_hp(damage)
        else:
            self.lose_hp(damage//2)
            
    def can_evolve(self) -> bool:
        '''
        Checks if Charmander has an evolved version
        Returns: True, as pokemon does have evolved version
        Worst case complexity: O(1) & Best Case complexity: O(1)
        ''' 
        return True
    
    def should_evolve(self) -> bool:
        '''
        Checks if Charmander is at the level of evolution
        Returns: True or False based on level
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''  
        return self.level >= 3
    
    def get_evolved_version(self):
        '''
        Gets the evolved version of the Charmander
        Returns: Charizard (evolved version of Charmander)
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''   
        return Charizard(self.lost_hp, self.original_order)
    
    def get_poke_name(self) -> str:
        '''
        Gets the name of the pokemon
        Returns: name of the pokemon as a string
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        return "Charmander"

class Venusaur(PokemonBase):
    
    pokedex_order = 3
    def __init__(self, lost_hp: int = 0, original_order: int|None = None):
        '''
        Initialises the constructor for Venusaur class

        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''        
        self.original_order = original_order
        self.lost_hp = lost_hp
        self.level = 2
        self.pokeType = "Grass"
        PokemonBase.__init__(self,self.get_hp() + self.lost_hp, self.pokeType)

    def get_speed(self) -> int:
        '''
        Gets the speed of the Venasaur
        Returns: speed of Venasaur based on level and pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''        
        return 3 + self.level // 2
    
    def get_hp(self) -> int:
        '''
        Gets the hp of the Venusaur
        Returns: hp of Venusaur based on level, pre-given value and lost hp
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''        
        return 20 + self.level // 2 - self.lost_hp
    
    def get_attack_damage(self) -> int:
        '''
        Gets the attack damage of the Venusaur
        Returns: attack damage of Venusaur based on pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''        
        return 5
    
    def get_defence(self) -> int:
        '''
        Gets the defence of the Venusaur
        Returns: defence of Venasaur based on pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        return 10
    
    def defend(self, damage: int) -> None:
        '''
        Venusaur uses defend to reduce incoming damage when possible
        Returns: None
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        if damage > self.get_defence() + 5:
            self.lose_hp(damage)
        else:
            self.lose_hp(damage // 2)
            
    def can_evolve(self) -> bool:
        '''
        Checks if Venusaur has an evolved version
        Returns: False, as pokemon does'nt have evolved version
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''  
        return False
    
    def should_evolve(self) -> bool:
        '''
        Checks if Venusaur is at the level of evolution
        Returns: False, as pokemon does'nt have evolved version
        Worst case complexity: O(1) & Best Case complexity: O(1)
        ''' 
        return False
    
    def get_evolved_version(self):
        '''
        Gets the evolved version of the Venusaur
        Returns: Exception as Venusaur does not have an evolved form
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''       
        raise Exception("Pokemon has no evolved version")
    
    def get_poke_name(self) -> str:
        '''
        Gets the name of the pokemon
        Returns: name of the pokemon as a string
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        return "Venusaur"

class Bulbasaur(PokemonBase):
    pokedex_order = 2
    def __init__(self, lost_hp: int = 0, original_order: int|None = None):
        '''
        Initialises the constructor for Bulbasaur class

        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''        
        self.original_order = original_order
        self.lost_hp = lost_hp
        self.level = 1
        self.pokeType = "Grass"
        PokemonBase.__init__(self,self.get_hp() + self.lost_hp, self.pokeType)

    def get_speed(self) -> int:
        '''
        Gets the speed of the Bulbasaur
        Returns: speed of Bulbasaur based on level and pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        return 7 + self.level // 2

    def get_hp(self) -> int:
        '''
        Gets the hp of the Bulbasaur
        Returns: hp of Bulbasaur based on level, pre-given value and lost hp
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        
        return 12 + self.level - self.lost_hp

    def get_attack_damage(self) -> int:
        '''
        Gets the attack damage of the Bulbasaur
        Returns: attack damage of Bulbasaur based on level and pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        return 5

    def get_defence(self) -> int:
        '''
        Gets the defence of the Bulbasaur
        Returns: defence of Bulbasaur based on pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        return 5

    def defend(self, damage: int) -> None:
        '''
        Bulbasaur uses defend to reduce incoming damage when possible
        Returns: None
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        if damage > self.get_defence() + 5:
            self.lose_hp(damage)
        else:
            self.lose_hp(damage // 2)
            
    def can_evolve(self) -> bool:
        '''
        Checks if Bulbasaur has an evolved version
        Returns: True, as pokemon does have evolved version
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''            
        return True
    
    def should_evolve(self) -> bool:
        '''
        Checks if Bulbasaur is at the level of evolution
        Returns: True or False based on level
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''   
        return self.level >= 2
    
    def get_evolved_version(self):
        '''
        Gets the evolved version of the Bulbasaur
        Returns: Venusaur (evolved version of Bulbasaur)
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''   
        return Venusaur(self.lost_hp, self.original_order)
    
    def get_poke_name(self) -> str:
        '''
        Gets the name of the pokemon
        Returns: name of the pokemon as a string
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        return "Bulbasaur"

class Blastoise(PokemonBase):
    pokedex_order = 5
    def __init__(self, lost_hp: int = 0, original_order: int|None = None):
        '''
        Initialises the constructor for Blastoise class

        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''        
        self.original_order = original_order
        self.lost_hp = lost_hp
        self.level = 3
        self.pokeType = "Water"
        PokemonBase.__init__(self,self.get_hp() + self.lost_hp, self.pokeType)
        
    def get_speed(self) -> int:
        '''
        Gets the speed of the Blastoise
        Returns: speed of Blastoise based on level and pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        return 10
    
    def get_hp(self) -> int:
        '''
        Gets the hp of the Blastoise
        Returns: hp of Blastoise based on level, pre-given value and lost hp
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''          
        return 15 + 2 * self.level - self.lost_hp
    
    def get_attack_damage(self) -> int:
        '''
        Gets the attack damage of the Blastiouse
        Returns: attack damage of Blastoise based on level and pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''   
        return 8 + self.level // 2
    
    def get_defence(self) -> int:
        '''
        Gets the defence of the Blastoise
        Returns: defence of Blastoise based on level and pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        return 8 + self.level
    
    def defend(self, damage: int) -> None:
        '''
        Blastoise uses defend to reduce incoming damage when possible
        Returns: None
        Worst case complexity: O(1) & Best Case complexity: O(1)
        ''' 
        if damage > 2 * self.get_defence():
            self.lose_hp(damage)
        else:
            self.lose_hp(damage // 2)
            
    def can_evolve(self) -> bool:
        '''
        Checks if Blastoise has an evolved version
        Returns: False, as pokemon does'nt have evolved version
        Worst case complexity: O(1) & Best Case complexity: O(1)
        ''' 
        return False
    
    def should_evolve(self) -> bool:
        '''
        Checks if Blastoise is at the level of evolution
        Returns: False, as pokemon does'nt have evolved version
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''     
        return False
    
    def get_evolved_version(self):
        '''
        Gets the evolved version of the Blastoise
        Returns: Exception as Blastoise does not have an evolved form
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''    
        raise Exception("Pokemon has no evolved version")
    
    def get_poke_name(self) -> str:
        '''
        Gets the name of the pokemon
        Returns: name of the pokemon as a string
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''   
        return "Blastoise"

class Squirtle(PokemonBase):
    pokedex_order = 4
    def __init__(self, lost_hp: int = 0, original_order: int|None = None):
        '''
        Initialises the constructor for Squirtle class

        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''        
        self.original_order = original_order
        self.lost_hp = lost_hp
        self.level = 1
        self.pokeType = "Water"
        PokemonBase.__init__(self,self.get_hp() + self.lost_hp, self.pokeType)
        
    def get_speed(self) -> int:
        '''
        Gets the speed of the Squirtle
        Returns: speed of Squirtle based on level and pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''           
        return 7
    
    def get_hp(self) -> int:
        '''
        Gets the hp of the Squirtle
        Returns: hp of Squirtle based on level, pre-given value and lost hp
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''          
        return 9 + 2 * self.level - self.lost_hp
    
    def get_attack_damage(self) -> int:
        '''
        Gets the attack damage of the Squirtle
        Returns: attack damage of Squirtle based on level and pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''            
        return 4 + self.level // 2
    
    def get_defence(self) -> int:
        '''
        Gets the defence of the Squirtle
        Returns: defence of Squirtle based on level and pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''   
        return 6 + self.level
    
    def defend(self, damage: int) -> None:
        '''
        Squirtle uses defend to reduce incoming damage when possible
        Returns: None
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        if damage > 2 * self.get_defence():
            self.lose_hp(damage)
        else:
            self.lose_hp(damage // 2)
            
    def can_evolve(self) -> bool:
        '''
        Checks if Squirtle has an evolved version
        Returns: True, as pokemon does have evolved version
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''    
        return True
    
    def should_evolve(self) -> bool:
        '''
        Checks if Squirtle is at the level of evolution
        Returns: True or False based on level
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''          
        return self.level >= 3
    
    def get_evolved_version(self):
        '''
        Gets the evolved version of the Squirtle
        Returns: Blastoise (evolved version of Squirtle)
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''   
        return Blastoise(self.lost_hp, self.original_order)
    
    def get_poke_name(self) -> str:
        '''
        Gets the name of the pokemon
        Returns: name of the pokemon as a string
        Worst case complexity: O(1) & Best Case complexity: O(1)
        ''' 
        return "Squirtle"


class Gengar(PokemonBase):
    pokedex_order = 8
    def __init__(self, lost_hp: int = 0, original_order: int|None = None):
        '''
        Initialises the constructor for Gengar class

        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        self.original_order = original_order
        self.lost_hp = lost_hp
        self.level = 3
        self.pokeType = "Ghost"
        PokemonBase.__init__(self,self.get_hp() + self.lost_hp, self.pokeType)
        
    def get_speed(self) -> int:
        '''
        Gets the speed of the Gengar
        Returns: speed of Gengar based on level and pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''  
        return 12
    
    def get_hp(self) -> int:
        '''
        Gets the hp of the Gengar
        Returns: hp of Gengar based on level, pre-given value and lost hp
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''  
        return 12 + self.level // 2 - self.lost_hp
    
    def get_attack_damage(self) -> int:
        '''
        Gets the attack damage of the Gengar
        Returns: attack damage of Gengar based on pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        return 18
    
    def get_defence(self) -> int:
        '''
        Gets the defence of the Gengar
        Returns: defence of Gengar based on pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        return 3
    
    def defend(self, damage: int) -> None:
        '''
        Gengar uses defend to reduce incoming damage when possible
        Returns: None
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        self.lose_hp(damage)
        
    def can_evolve(self) -> bool:
        '''
        Checks if Gengar has an evolved version
        Returns: False, as pokemon does'nt have evolved version
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''  
        return False
    
    def should_evolve(self) -> bool:
        '''
        Checks if Gengar is at the level of evolution
        Returns: False, as pokemon does'nt have evolved version
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''   
        return False
    
    def get_evolved_version(self):
        '''
        Gets the evolved version of the Gengar
        Returns: Exception as Gengar does not have an evolved form
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''  
        raise Exception("Pokemon has no evolved version")
    
    def get_poke_name(self) -> str:
        '''
        Gets the name of the pokemon
        Returns: name of the pokemon as a string
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''  
        return "Gengar"

class Haunter(PokemonBase):
    pokedex_order = 7
    def __init__(self, lost_hp: int = 0, original_order: int|None = None):
        '''
        Initialises the constructor for Haunter class

        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        self.original_order = original_order
        self.lost_hp = lost_hp
        self.level = 1
        self.pokeType = "Ghost"
        PokemonBase.__init__(self,self.get_hp() + self.lost_hp, self.pokeType)
        
    def get_speed(self) -> int:
        '''
        Gets the speed of the Haunter
        Returns: speed of Haunter based on level and pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        ''' 
        return 6
    
    def get_hp(self) -> int:
        '''
        Gets the hp of the Haunter
        Returns: hp of Gengar based on level, pre-given value and lost hp
        Worst case complexity: O(1) & Best Case complexity: O(1)
        ''' 
        return 9 + self.level // 2 - self.lost_hp
    
    def get_attack_damage(self) -> int:
        '''
        Gets the attack damage of the Haunter
        Returns: attack damage of Haunter based on pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        return 8
    
    def get_defence(self) -> int:
        '''
        Gets the defence of the Haunter
        Returns: defence of Haunter based on pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        return 6
    
    def defend(self, damage: int) -> None:
        '''
        Haunter uses defend to reduce incoming damage when possible
        Returns: None
        Worst case complexity: O(1) & Best Case complexity: O(1)
        ''' 
        self.lose_hp(damage)
        
    def can_evolve(self) -> bool:
        '''
        Checks if Haunter has an evolved version
        Returns: True, as pokemon does have evolved version
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''  
        return True
    
    def should_evolve(self) -> bool:
        '''
        Checks if Haunter is at the level of evolution
        Returns: True or False based on level
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''  
        return self.level >= 3
    
    def get_evolved_version(self):
        '''
        Gets the evolved version of the Haunter
        Returns: Gengar (evolved version of Haunter)
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''   
        return Gengar(self.lost_hp, self.original_order)
    
    def get_poke_name(self) -> str:
        '''
        Gets the name of the pokemon
        Returns: name of the pokemon as a string
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''            
        return "Haunter"

class Gastly(PokemonBase):
    pokedex_order = 6
    def __init__(self, lost_hp: int = 0, original_order: int|None = None):
        '''
        Initialises the constructor for Gastly class

        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''        
        self.original_order = original_order
        self.lost_hp = lost_hp
        self.level = 1
        self.pokeType = "Ghost"
        PokemonBase.__init__(self,self.get_hp() + self.lost_hp, self.pokeType)

    def get_speed(self) -> int:
        '''
        Gets the speed of the Gastly
        Returns: speed of Gastly based on level and pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''    
        return 2
    
    def get_hp(self) -> int:
        '''
        Gets the hp of the Gastly
        Returns: hp of Gastly based on level, pre-given value and lost hp
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''      
        return 6 + self.level // 2 - self.lost_hp
    
    def get_attack_damage(self) -> int:
        '''
        Gets the attack damage of the Gastly
        Returns: attack damage of Gaslty based on pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''      
        return 4
    
    def get_defence(self) -> int:
        '''
        Gets the defence of the Gastly
        Returns: defence of Gastly based on pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''           
        return 8
    
    def defend(self, damage: int) -> None:
        '''
        Gastly uses defend to reduce incoming damage when possible
        Returns: None
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''             
        self.lose_hp(damage)
        
    def can_evolve(self) -> bool:
        '''
        Checks if Gastly has an evolved version
        Returns: True, as pokemon does have evolved version
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''       
        return True
    
    def should_evolve(self) -> bool:
        '''
        Checks if Gastly is at the level of evolution
        Returns: True or False based on level
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''  
        return self.level >= 1
    
    def get_evolved_version(self):
        '''
        Gets the evolved version of the Gastly
        Returns: Haunter (evolved version of Gastly)
        Worst case complexity: O(1) & Best Case complexity: O(1)
        ''' 
        return Haunter(self.lost_hp, self.original_order)
    
    def get_poke_name(self) -> str:
        '''
        Gets the name of the pokemon
        Returns: name of the pokemon as a string
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''  
        return "Gastly"


class Eevee(PokemonBase):
    pokedex_order = 9
    def __init__(self, lost_hp: int = 0, original_order: int|None = None):
        '''
        Initialises the constructor for Eevee class

        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''        
        self.original_order = original_order
        self.lost_hp = lost_hp
        self.level = 1
        self.pokeType = "Normal"
        PokemonBase.__init__(self,self.get_hp() + self.lost_hp, self.pokeType)

    def get_speed(self) -> int:
        '''
        Gets the speed of Eevee
        Returns: speed of Eevee based on level and pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''       
        return 7 + self.level
    
    def get_hp(self) -> int:
        '''
        Gets the hp of the Eevee
        Returns: hp of Eevee based on level, pre-given value and lost hp
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        return 10 - self.lost_hp
    
    def get_attack_damage(self) -> int:
        '''
        Gets the attack damage of the Eevee
        Returns: attack damage of Eevee based on level and pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        return 6 + self.level
    
    def get_defence(self) -> int:
        '''
        Gets the defence of the Eevee
        Returns: defence of Eevee based on level and pre-given value
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        return 4 + self.level
    
    def defend(self, damage: int) -> None:
        '''
        Eevee uses defend to reduce incoming damage when possible
        Returns: None
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''    
        if damage >= self.get_defence():
            self.lose_hp(damage)
        else:
            self.lose_hp(0)
            
    def can_evolve(self) -> bool:
        '''
        Checks if Eevee has an evolved version
        Returns: False, as pokemon does'nt have evolved version
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''      
        return False
    
    def should_evolve(self) -> bool:
        '''
        Checks if Eevee is at the level of evolution
        Returns: False, as pokemon does'nt have evolved version
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''     
        return False
    
    def get_evolved_version(self):
        '''
        Gets the evolved version of the Eevee
        Returns: Exception as Eevee does not have an evolved form
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''  
        raise Exception("Pokemon has no evolved version")
    
    def get_poke_name(self) -> str:
        '''
        Gets the name of the pokemon
        Returns: name of the pokemon as a string
        Worst case complexity: O(1) & Best Case complexity: O(1)
        '''
        return "Eevee"
