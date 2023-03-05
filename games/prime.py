import math
import random
from typing import ClassVar

from simple_term_menu import TerminalMenu

from games.common import BaseGame
from games.constants import NOT_PRIME_CHOICE, PRIME_CHOICE


class PrimeGame(BaseGame):
    MIN_VALUE: ClassVar[int] = 10
    MAX_VALUE: ClassVar[int] = 100
    ANSWER_CHOICES: ClassVar[list[str]] = (NOT_PRIME_CHOICE, PRIME_CHOICE)

    def get_win_message(self):
        return 'Поздравляем, вы 3 раза ответили правильно!'

    def start(self):
        print('Добро пожаловать в игру простое число!')
        self.menu = TerminalMenu(self.ANSWER_CHOICES)

    def __check_is_simple(self, number: int) -> bool:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    def __ask_choice(self, right_answer: bool, number: int) -> None:
        print(f'Число {number} - простое или не простое?')
        
        answer = self.menu.show()
        
        if bool(answer) == right_answer:
            print('Вы ответили правильно!')
            self.wins_count += 1
        else:
            print('К сожалению это не правильный ответ')
        self._check_win()

    def update(self):
        number = random.randint(self.MIN_VALUE, self.MAX_VALUE)
        right_answer = self.__check_is_simple(number)
        
        self.__ask_choice(right_answer, number)
        
