from pokemon import Blastoise, Bulbasaur, Charizard, Charmander, Eevee, Gastly, Squirtle, Venusaur
from tests.base_test import BaseTest

class TestPokemon(BaseTest):

    def test_venusaur_stats(self):
        v = Venusaur()
        self.assertEqual(v.get_hp(), 21)
        self.assertEqual(v.get_level(), 2)
        self.assertEqual(v.get_attack_damage(), 5)
        self.assertEqual(v.get_speed(), 4)
        self.assertEqual(v.get_defence(), 10)
        v.level_up()
        v.level_up()
        v.level_up()
        self.assertEqual(v.get_hp(), 22)
        self.assertEqual(v.get_level(), 5)
        self.assertEqual(v.get_attack_damage(), 5)
        self.assertEqual(v.get_speed(), 5)
        self.assertEqual(v.get_defence(), 10)
        v.lose_hp(5)

        self.assertEqual(str(v), "LV. 5 Venusaur: 17 HP")
    
    def test_get_Name(self):
        ''' Tests the get_poke_name method for 3 scenarios
            Scenario 1: Default name
            Scenario 2: name after evolving once
            Scenario 3: name after evolving twice        
        '''
        s = Squirtle()
        self.assertEqual(s.get_poke_name(), "Squirtle")
        b = Bulbasaur()
        b = b.get_evolved_version()
        self.assertEqual(b.get_poke_name(), "Venusaur")
        g = Gastly()
        g = g.get_evolved_version()
        g = g.get_evolved_version()
        self.assertEqual(g.get_poke_name(), "Gengar")

    def test_get_pokeType(self):
        '''Tests the get_pokeType method '''
        b = Bulbasaur()
        self.assertEqual(b.pokeType, "Grass")
        e = Eevee()
        self.assertEqual(e.pokeType, "Normal")
        c = Charizard()
        self.assertEqual(c.pokeType, "Fire")
    
    def test_get_level(self):
        '''Tests the get_level method in 3 pokemon'''
        g = Gastly()
        self.assertEqual(g.get_level(), 1)
        g = g.get_evolved_version()
        g = g.get_evolved_version()
        self.assertEqual(g.get_level(), 3)
        c = Charmander()
        c.level_up()
        self.assertEqual(c.get_level(), 2)
        e = Eevee()
        e.level_up()
        e.level_up()
        e.level_up()
        e.level_up()
        e.level_up()
        e.level_up()
        self.assertEqual(e.get_level(), 7)

    def test_get_hp(self):
        '''Tests the get_hp method for 3 different scenarios
            Scenario 1: base stat
            Scenario 2: After leveling up
            Scenario 3: Including health lost
        '''
        e = Eevee()
        self.assertEqual(e.get_hp(), 10)
        c = Charizard()
        c.level_up()
        self.assertEqual(c.get_hp(), 16)
        b = Blastoise(2)
        self.assertEqual(b.get_hp(), 19)

    def test_get_attack(self):
        '''Tests the get_attack_damage method for 3 scenarios
            Scenario 1: base stat
            Scenario 2: After leveling up
            Scenario 3: After leveling up'''
        e = Eevee()
        self.assertEqual(e.get_attack_damage(), 7)
        e.level_up()
        e.level_up()
        e.level_up()
        self.assertEqual(e.get_attack_damage(), 10)
        b = Blastoise()
        b.level_up()
        self.assertEqual(b.get_attack_damage(), 10)

    def test_get_speed(self):
        '''Tests get_speek method for 3 different pokemon in three different scenarios
            scenario 1: Base stats
            scenario 2: after leveling up
            scenario 3: after evolving
        '''
        b = Bulbasaur()
        self.assertEqual(b.get_speed(), 7)
        e = Eevee()
        e.level_up()
        e.level_up()
        e.level_up()
        self.assertEqual(e.get_speed(), 11)
        c = Charmander()
        c = c.get_evolved_version()
        self.assertEqual(c.get_speed(), 12)

    def test_get_defence(self):
        '''Tests get_defence method for differnt pokeomen and in different scenarios
            Scenario 1: Base stat
            Scenario 2: After leveling up
            Scenario 3: After evloving
        '''
        s = Squirtle()
        self.assertEqual(s.get_defence(), 7)
        s.level_up()
        s.level_up()
        self.assertEqual(s.get_defence(), 9)
        b = Bulbasaur()
        b = b.get_evolved_version()
        self.assertEqual(b.get_defence(), 10)

    def test_defence_calculation(self):
        '''Tests the defence_calculation method for a pokemon in 3 scenarios
            Scenario 1: if attacking damage = 0
            Scenario 2: if attacking damage is over threshold
            Scenario 3: if attacking damage is under threshold
        '''
        v = Venusaur()
        v.defend(0)
        self.assertEqual(v.get_hp(), 21)
        v.defend(20)
        self.assertEqual(v.get_hp(), 1)
        v.heal()
        v.defend(10)
        self.assertEqual(v.get_hp(), 16)
