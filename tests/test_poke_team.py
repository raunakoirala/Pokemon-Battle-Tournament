from poke_team import Action, Criterion, PokeTeam
from random_gen import RandomGen
from pokemon import Bulbasaur, Charizard, Charmander, Gastly, Squirtle, Eevee
from tests.base_test import BaseTest

class TestPokeTeam(BaseTest):

    def test_random(self):
        RandomGen.set_seed(123456789)
        t = PokeTeam.random_team("Cynthia", 0)
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Squirtle, Gastly, Eevee, Eevee, Eevee, Eevee]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)

    def test_regen_team(self):
        RandomGen.set_seed(123456789)
        t = PokeTeam.random_team("Cynthia", 2, team_size=4, criterion=Criterion.HP)
        # This should end, since all pokemon are fainted, slowly.
        while not t.is_empty():
            p = t.retrieve_pokemon()
            p.lose_hp(1)
            t.return_pokemon(p)
        t.regenerate_team()
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Bulbasaur, Eevee, Charmander, Gastly]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)

    def test_battle_option_attack(self):
        t = PokeTeam("Wallace", [1, 0, 0, 0, 0], 1, PokeTeam.AI.ALWAYS_ATTACK)
        p = t.retrieve_pokemon()
        e = Eevee()
        self.assertEqual(t.choose_battle_option(p, e), Action.ATTACK)

    def test_special_mode_1(self):
        t = PokeTeam("Lance", [1, 1, 1, 1, 1], 1, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        # C B S G E
        t.special()
        # S G E B C
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Squirtle, Gastly, Eevee, Bulbasaur, Charmander]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)

    def test_string(self):
        t = PokeTeam("Dawn", [1, 1, 1, 1, 1], 2, PokeTeam.AI.RANDOM, Criterion.DEF)
        self.assertEqual(str(t), "Dawn (2): [LV. 1 Gastly: 6 HP, LV. 1 Squirtle: 11 HP, LV. 1 Eevee: 10 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Charmander: 9 HP]")

    def test_init1(self):
        """
        Tests whether an instance of PokeTeam is generated
        """
        t = PokeTeam("Fred", [1,2,1,1,0], 1, PokeTeam.AI.ALWAYS_ATTACK)
        self.assertIsInstance(t,PokeTeam)

    def test_init2(self):
        """
        Tests for correct pokemon generated
        """
        t = PokeTeam("Fred", [1,2,1,1,0], 1, PokeTeam.AI.ALWAYS_ATTACK)
        pokemon = []
        expected_classes = [Charmander, Bulbasaur, Bulbasaur, Squirtle, Gastly]
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        for i in range(len(expected_classes)):
            self.assertIsInstance(pokemon[i],expected_classes[i])

    def test_init3(self):
        """
        Tests for correct battle mode used
        """
        t = PokeTeam("Fred", [1, 2, 1, 1, 0], 1, PokeTeam.AI.ALWAYS_ATTACK)
        self.assertEqual(t.battle_mode, 1)
    def test_randomteam1(self):
        """
        Tests for correct team size
        """
        size = 5
        RandomGen.set_seed(1)
        t = PokeTeam.random_team("Fred", 0, size)
        self.assertEqual(len(t.team),size)

    def test_randomteam2(self):
        """
        Tests for correct team pokemon
        """
        size = 5
        RandomGen.set_seed(1)
        t = PokeTeam.random_team("Fred", 0, size)
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Charmander, Bulbasaur, Bulbasaur, Squirtle, Gastly]
        for i in range(len(expected_classes)):
            self.assertIsInstance(pokemon[i], expected_classes[i])

    def test_randomteam3(self):
        """
        Tests for correct default ai type
        """
        size = 5
        RandomGen.set_seed(1)
        t = PokeTeam.random_team("Fred", 0, size)
        self.assertEqual(t.ai_type, PokeTeam.AI.RANDOM)

    def test_retrieve1(self):
        """
        Tests retrieving for battlemode 0
        """
        t = PokeTeam("Fred", [0,1,1,1,2], 0, PokeTeam.AI.ALWAYS_ATTACK)
        self.assertIsInstance(t.retrieve_pokemon(),Bulbasaur)

    def test_retrieve2(self):
        """
        Tests retrieving for battlemode 1
        """
        t = PokeTeam("Fred", [1,0,2,0,2], 1, PokeTeam.AI.ALWAYS_ATTACK)
        self.assertIsInstance(t.retrieve_pokemon(), Charmander)

    def test_retrieve3(self):
        """
        Tests retrieving for battlemode 2
        """
        t = PokeTeam("Fred", [1,0,2,0,2], 2, PokeTeam.AI.ALWAYS_ATTACK, Criterion.HP)
        self.assertIsInstance(t.retrieve_pokemon(), Squirtle)

    def test_return1(self):
        """
        Tests return for battlemode 0
        """
        t = PokeTeam("Fred", [1,0,2,0,2], 0, PokeTeam.AI.ALWAYS_ATTACK)
        t.return_pokemon(t.retrieve_pokemon())
        self.assertIsInstance(t.retrieve_pokemon(),Charmander)

    def test_return2(self):
        """
        Tests return for battlemode 1
        """
        t = PokeTeam("Fred", [1, 0, 2, 0, 2], 1, PokeTeam.AI.ALWAYS_ATTACK)
        t.return_pokemon(t.retrieve_pokemon())
        self.assertIsInstance(t.retrieve_pokemon(), Squirtle)

    def test_return3(self):
        """
        Tests return for battlemode 2. Eevee is levelled up to increase defence
        """
        t = PokeTeam("Fred", [1, 1, 1, 0, 2], 2, PokeTeam.AI.ALWAYS_ATTACK, Criterion.DEF)
        first = t.retrieve_pokemon()
        second = t.retrieve_pokemon()
        for i in range(10):
            second.level_up()
        t.return_pokemon(first)
        t.return_pokemon(second)
        self.assertIsInstance(t.retrieve_pokemon(), Eevee)

    def test_special1(self):
        """
        Tests battlemode 0 special
        """
        t = PokeTeam("Fred", [1, 1, 1, 0, 2], 0, PokeTeam.AI.ALWAYS_ATTACK)
        t.special()
        self.assertIsInstance(t.retrieve_pokemon(), Eevee)

    def test_special2(self):
        """
        Tests battlemode 1 special
        """
        t = PokeTeam("Fred", [1, 1, 1, 0, 2], 1, PokeTeam.AI.ALWAYS_ATTACK)
        t.special()
        self.assertIsInstance(t.retrieve_pokemon(), Squirtle)

    def test_special3(self):
        """
        Tests battlemode 2 special
        """
        t = PokeTeam("Fred", [1, 1, 1, 1, 0], 2, PokeTeam.AI.ALWAYS_ATTACK, Criterion.HP)
        t.special()
        self.assertIsInstance(t.retrieve_pokemon(), Gastly)

    def test_regen_team1(self):
        """
        Tests regenerating a team
        """
        t = PokeTeam("Fred", [1, 1, 1, 1, 0], 2, PokeTeam.AI.ALWAYS_ATTACK, Criterion.HP)
        for i in range(4):
            t.retrieve_pokemon()
        t.regenerate_team()
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        self.assertEqual(len(pokemon), 4)

    def test_regen_team2(self):
        """
        Tests regenerating a team
        """
        t = PokeTeam("Fred", [1, 1, 1, 1, 0], 2, PokeTeam.AI.ALWAYS_ATTACK, Criterion.HP)
        for i in range(4):
            t.retrieve_pokemon()
        t.regenerate_team()
        pokemon = []
        expected_classes = [Bulbasaur, Squirtle, Charmander, Gastly]
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        for i in range(len(pokemon)):
            self.assertIsInstance(pokemon[i],expected_classes[i])

    def test_regen_team3(self):
        """
        Tests regenerating a team
        """
        t = PokeTeam("Fred", [1, 1, 1, 1, 0], 1, PokeTeam.AI.ALWAYS_ATTACK, Criterion.HP)
        for i in range(4):
            t.retrieve_pokemon()
        t.regenerate_team()
        self.assertEqual(t.battle_mode, 1)

    def test_str1(self):
        """
        Tests string representation
        """
        t = PokeTeam("Fred", [1, 1, 1, 1, 0], 2, PokeTeam.AI.ALWAYS_ATTACK, Criterion.HP)
        self.assertEqual(str(t), "Fred (2): [LV. 1 Bulbasaur: 13 HP, LV. 1 Squirtle: 11 HP, LV. 1 Charmander: 9 HP, LV. 1 Gastly: 6 HP]")

    def test_str2(self):
        """
        Tests string representation
        """
        t = PokeTeam("Fred", [1, 1, 1, 1, 1], 1, PokeTeam.AI.ALWAYS_ATTACK)
        self.assertEqual(str(t), "Fred (1): [LV. 1 Charmander: 9 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Squirtle: 11 HP, LV. 1 Gastly: 6 HP, LV. 1 Eevee: 10 HP]")

    def test_str3(self):
        """
        Tests string representation
        """
        t = PokeTeam("Fred", [2, 0, 1, 1, 1], 0, PokeTeam.AI.ALWAYS_ATTACK)
        self.assertEqual(str(t), "Fred (0): [LV. 1 Charmander: 9 HP, LV. 1 Charmander: 9 HP, LV. 1 Squirtle: 11 HP, LV. 1 Gastly: 6 HP, LV. 1 Eevee: 10 HP]")

    def test_isempty1(self):
        """
        Tests is_empty method
        """
        t = PokeTeam("Fred", [2, 0, 1, 1, 1], 0, PokeTeam.AI.ALWAYS_ATTACK)
        for i in range(5):
            t.retrieve_pokemon()
        self.assertEqual(t.is_empty(),True)

    def test_isempty2(self):
        """
        Tests is_empty method
        """
        t = PokeTeam("Fred", [1, 0, 1, 0, 1], 1, PokeTeam.AI.ALWAYS_ATTACK)
        for i in range(3):
            t.retrieve_pokemon()
        self.assertEqual(t.is_empty(),True)

    def test_isempty3(self):
        """
        Tests is_empty method
        """
        t = PokeTeam("Fred", [1, 0, 1, 1, 1], 0, PokeTeam.AI.ALWAYS_ATTACK)
        for i in range(2):
            t.retrieve_pokemon()
        self.assertEqual(t.is_empty(), False)

    def test_choose_battle_option1(self):
        """
        Tests choose_battle_option method
        """
        t = PokeTeam("Fred", [1, 0, 1, 1, 1], 0, PokeTeam.AI.ALWAYS_ATTACK)
        self.assertEqual(t.choose_battle_option(t.retrieve_pokemon(),Charmander()),Action.ATTACK)

    def test_choose_battle_option2(self):
        """
        Tests choose_battle_option method
        """
        RandomGen.set_seed(3)
        t = PokeTeam("Fred", [1, 0, 1, 1, 1], 0, PokeTeam.AI.RANDOM)
        self.assertEqual(t.choose_battle_option(t.retrieve_pokemon(),Charmander()),Action.HEAL)

    def test_choose_battle_option3(self):
        """
        Tests choose_battle_option method
        """
        RandomGen.set_seed(3)
        t = PokeTeam("Fred", [1, 0, 1, 1, 1], 1, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        self.assertEqual(t.choose_battle_option(t.retrieve_pokemon(),Squirtle()),Action.SWAP)