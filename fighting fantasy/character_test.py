import pytest
import random
from fighting_fantasy import Character,PlayerCharacter,Game


class TestCharacter():
    @pytest.fixture
    def characters(self):
        random.seed(6082008)
        return [Character('Orc',10,16),
                Character('Dragon',12,22),
                ]

    def test_character(self, characters):
        orc,dragon = characters

        assert orc.skill==10
        assert orc.__repr__()=='character name="Orc", skill=10 and stamina=16'

    def test_is_dead(self, characters):
        orc,dragon = characters
        assert orc.is_dead==False

    def test_set_is_dead(self, characters):
        orc,dragon = characters
        assert orc.set_is_dead==0

    def test_wound(self,characters):
        orc,dragon = characters
        orc.wound()
        assert orc.stamina==14

    def test_score(self, characters):
        orc,dragon = characters
        random.seed(6082008)
        assert orc.score==random.randint(2.12)


class TestPlayerCharacter():
    @pytest.fixture
    def hero(self):
        random.seed(6082008)
        return PlayerCharacter.generate_char('Panda')


    def test_character(self, hero):
        random.seed(6082008)
        panda = hero

        assert panda.hero_status()==(f'The hero is called Panda, they have {6 + random.randint(1, 6)} skill, '
                                     f'{12 + random.randint(2, 12)} stamina and '
                                     f'{ 6 + random.randint(1, 6)} potions')


class TestGame():
    @pytest.fixture
    def game(self):
        random.seed(6082008)
        game=Game()
        return game

