import random
from typing import ClassVar

from games.common import BaseGame
from games.constants import EVEN_CHOICE, ODD_CHOICE

from simple_term_menu import TerminalMenu


class OddEvenGame(BaseGame):
    ANSWER_CHOICES: ClassVar[list[str]] = (EVEN_CHOICE, ODD_CHOICE)

    def get_win_message(self):
        return f'ВЫ правильно ответили {self.wins_count} раза!'

    def start(self):
        print('Добро пожаловать в игру Чёт/Нечёт!')
        self.menu = TerminalMenu(self.ANSWER_CHOICES)

    def __ask_choice(self, number: int) -> None:
        print(number)
        chosen_option = self.menu.show()

        if chosen_option == number % 2:
            self.wins_count += 1
            print('Это правильный ответ!')
        else:
            print('Вы ошиблись.')

        self._check_win()
        print('===========================')

    def update(self):
        print('Число ниже чётное или не чётное?')
        number = random.randint(2, 10000000)
        self.__ask_choice(number)
