import math
import random
from typing import ClassVar

from games.common import BaseGame


class GCDGame(BaseGame):
    MIN_VALUE: ClassVar[int] = 10
    MAX_VALUE: ClassVar[int] = 100
    GCD_NUMBERS_COUNT: ClassVar[int] = 2

    def get_win_message(self):
        return f'ВЫ правильно ответили {self.wins_count} раза!'

    def start(self):
        print('Добро пожаловать в игру Наибольший Общий Делитель!')

    def _get_random_number_in_range(self):
        return random.randint(self.MIN_VALUE, self.MAX_VALUE)

    def __ask_choice(self, right_answer: str, *numbers):
        answer = input(f'Наибольший общий делитель чисел {numbers}:\t')
        
        if answer != right_answer:
            print(f'К сожалению вы ошиблись. Правильный ответ: {right_answer}')
        else:
            print('Это правильный ответ! Отлично!')
            self.wins_count += 1
        
        self._check_win()

    def update(self):
        numbers = [self._get_random_number_in_range() for _ in range(self.GCD_NUMBERS_COUNT)]
        right_answer = str(math.gcd(*numbers))

        self.__ask_choice(right_answer, *numbers)
