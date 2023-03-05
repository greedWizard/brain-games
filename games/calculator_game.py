from typing import ClassVar
from games.common import BaseGame
from games.mixins import GenerateMathPatternMixin


class CalculatorGame(BaseGame, GenerateMathPatternMixin):
    OPERATIONS_LIST: ClassVar[list[str]] = GenerateMathPatternMixin.OPERATIONS_LIST + [
        '/',
    ]
    MIN_NUMBER_IN_EXPRESSION: ClassVar[int] = 0
    MAX_NUMBER_IN_EXPRESSION: ClassVar[int] = 1000
    SEQUENCE_OPERATIONS_COUNT: ClassVar[int] = 4
    
    def get_win_message(self):
        return 'Поздравляем, вы 3 раза ответили правильно!'
    
    def start(self):
        print('Добро пожаловать в игру калькулятор!')

    def __ask_choice(self, right_answer: str, sequence_str: str):
        print('=========================')
        choice = input(f'{sequence_str}=\t')
        
        if choice == right_answer:
            print('Правильный ответ! Отлично!')
            self.wins_count += 1
        else:
            print('К сожалению ответ не правильный')

    def update(self):
        print('Посчитайте выражение на экране (округлите до целых):')

        sequence_function, sequence_str = self._generate_math_expression(
            allow_parameter=False,
            sequence_operations_count=self.SEQUENCE_OPERATIONS_COUNT,
        )
        right_answer = str(int(sequence_function()))
        self.__ask_choice(right_answer, sequence_str)
        self._check_win()
        