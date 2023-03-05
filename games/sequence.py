from typing import Callable, ClassVar, Literal, SupportsInt
import random

from games.common import BaseGame
from games.mixins import GenerateMathPatternMixin


class SequenceGame(BaseGame, GenerateMathPatternMixin):
    ELEMENTS_IN_SEQUENCE_COUNT: ClassVar[Literal[5]] = 8
    
    def get_win_message(self):
        return f'Поздравляем! Вы отгадали {self.wins_count} правильные последовательности!'

    def __ask_choice(self, right_answer: str, initial_sequence: str, sequence_function_str: str) -> None:
        print('=======================================')
        print('Угадайте пропущенное число в предоставленной последовательности:')
        print(initial_sequence)
        choice = input()
        
        if choice != right_answer:
            print('К сожалению вы ошиблись.')
            print(f'Правильным ответом было: {right_answer}')
            print(f'Изначальная функция последовательности: {sequence_function_str}')
        else:
            print('Поздравляю, вы выбрали правильный ответ!')
            self.wins_count += 1

    def update(self):
        sequence_str, sequence, right_answer = self.__get_sequence_data()

        self.__ask_choice(right_answer, sequence, sequence_str)
        self._check_win()

    def __get_sequence_data(self) -> tuple[str, Callable[[SupportsInt], SupportsInt], str]:
        ''' Создать новую последовательность и получить её функцию для вывода ответа и праивльный ответ '''
        sequence_function, sequence_str = self._generate_math_expression(
            allow_parameter=True,
            sequence_operations_count=self.SEQUENCE_OPERATIONS_COUNT,
        )

        sequence = ''
        missing_element_index = random.randint(0, 4)
        right_answer = ''
        
        for index, _ in enumerate(range(self.ELEMENTS_IN_SEQUENCE_COUNT)):
            pattern = str(sequence_function(index))
        
            if index == missing_element_index:
                right_answer = pattern
                pattern = '...'
            
            sequence = ' '.join((sequence, pattern))
        return sequence_str, sequence, right_answer
    
    def start(self) -> None:
        print('Добро пожаловать в игру угадай число в последовательности!')
