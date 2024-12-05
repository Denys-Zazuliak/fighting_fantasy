import random


# import tkinter as tk
#
# root=tk.Tk()
# root.title('BATTLE')
# root.geometry("1000x750")


class Character:
    def __init__(self, name, skill, stamina):
        self.name = name
        self.skill = skill
        self.stamina = stamina
        self.dice_sum = 0

    def __repr__(self):
        return (f'character name="{self.name}", skill={self.skill} and stamina={self.stamina}')

    def score(self):
        self.dice_sum = 0

        for _ in range(2):
            self.dice_sum += random.randint(1, 6)

        return (self.skill + self.dice_sum), self.dice_sum

    def wound(self, damage: int = 2):
        self.stamina = self.stamina - damage
        return (f'{self.name} has taken {damage} points of damage')

    @property
    def is_dead(self):
        return self.stamina <= 0

    @is_dead.setter
    def set_is_dead(self, dead):
        if dead:
            self.stamina = 0
        else:
            self.stamina = max(self.stamina, 1)


#         return self.stamina


class PlayerCharacter(Character):
    def __init__(self, name, skill=0, stamina=0, potion=0):
        super().__init__(name, skill, stamina)
        self.potion = potion

    @classmethod
    def generate_char(cls, name):
        stamina = 6 + random.randint(1, 6)
        skill = 12 + random.randint(2, 12)
        potion = 6 + random.randint(1, 6)
        return cls(name, stamina, skill, potion)

    def hero_status(self):
        return (
            f'The hero is called {self.name}, they have {self.skill} skill, {self.stamina} stamina and {self.potion} potions \n')


class Game:
    def __init__(self):
        self.enemy = None
        self.hero = None
        self.result = None
        self.round_result = None

    def choose_enemy(self):
        creatures = [Character('Orc', 10, 20),
                     Character('Goblin', 7, 13),
                     Character('Human', 12, 17)]
        self.enemy = random.choice(creatures)
        creatures.remove(self.enemy)

        return self.enemy

    def choose_hero(self, hero):
        self.hero = hero

    def fight_round(self):
        outcome = ''
        hero_score = self.hero.score()
        enemy_score = self.enemy.score()
        if hero_score[0] < enemy_score[0]:
            self.hero.wound()
            outcome = f'{self.hero.name} has taken 2 stamina damage! They now have {self.hero.stamina} stamina left \n'
        elif hero_score[0] == enemy_score[0]:
            self.hero.wound(1)
            self.enemy.wound(1)
            outcome = f'Both {self.hero.name} and {self.enemy.name} have taken damage! \n'
        else:
            self.enemy.wound()
            outcome = f'{self.enemy.name} has taken 2 stamina damage! They now have {self.enemy.stamina} stamina left \n'

        return [hero_score, enemy_score, outcome]

    def resolve_fight(self):
        self.round_result = game.fight_round()

        return self.round_result

    def battle_status(self):
        print(f'{self.hero.name} and {self.enemy.name} are fighting \n')
        print(
            f'{self.hero.name} has {self.hero.skill} skill, {self.hero.stamina} stamina and {self.hero.potion} potions')
        print(f'{self.enemy.name} has {self.enemy.skill} skill and {self.enemy.stamina} stamina')

    def get_round_result(self):
        print(f'{self.hero.name} has rolled {self.round_result[0][1]} for the total score of {self.round_result[0][0]}')
        print(
            f'{self.enemy.name} has rolled {self.round_result[1][1]} for the total score of {self.round_result[1][0]}')
        print(f'{self.round_result[2]} \n')


class GameCLI:
    def __init__(self):
        self.game = Game()

    def run_game(self):
        print('Welcome to Fighting Fantasy Battle')

        name = input('Enter the name for your character: ')

        hero = PlayerCharacter.generate_char(name)

        print(f'Welcome {name}')

        return hero

if __name__ == "__main__":
    GameCLI()

choice = 'y'

cli=GameCLI()
game = Game()
opponent = game.choose_enemy()
player=cli.run_game()
game.choose_hero(player)
# print(dragon.__repr__())
# print(dragon.hero_status())

game.battle_status()
while (not (player.is_dead)) and (not (opponent.is_dead)) and (choice.lower() == 'y'):
    choice = input('Would you like to fight a round?(y/n) ')

    if choice.lower() == 'y':
        game.resolve_fight()
        game.get_round_result()
    elif choice.lower() == 'n':
        print('You flee in terror!')

if player.is_dead:
    print(f'{player.name} has died!')
elif opponent.is_dead:
    print(f'{opponent.name} has died!')

# battle_label=tk.Label(root,
#                  text=f'{dragon.name} and {default_enemy.name} are fighting',
#                  anchor=tk.CENTER,
#                  bg="lightblue",
#                  height=1,
#                  width=30,
#                  bd=3,
#                  font=("Arial", 16, "bold"),
#                  fg="black",
#                  padx=15,
#                  pady=15
#                 )
# battle_label.pack(pady=20)
#
#
#     def char_label(self,window):
#         char=tk.Label(window,
#                  text=f'{self.__repr__()}',
#                  anchor=tk.CENTER,
#                  bg="lightblue",
#                  height=1,
#                  width=40,
#                  bd=2,
#                  font=("Arial", 8, "bold"),
#                  fg="black"
#                 )
#         char.pack(padx=50,pady=10)
# #
#     def chat_button(self,window):
#         button = tk.Button(window,
#                    text="Dragon score",
#                    command=dragon.score(),
#                    anchor="center",
#                    bd=3,
#                    wraplength=100)
#         button.pack(padx=20, pady=20)
#
#
# dragon.char_label(root)
# dragon.chat_button(root)
# #
# root.mainloop()

