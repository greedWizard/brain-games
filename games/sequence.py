from typing import Callable, ClassVar, Literal, SupportsInt
import random

from games.common import BaseGame
from games.constants import RIGHT_ANSWERS_TO_WIN_COUNT
from games.exceptions import StopGameException


class SequenceGame(BaseGame):
    OPERATIONS_LIST: ClassVar[list[str]] = [
        '+',
        '-',
        '*',
    ]
    VARIABLE_CHAR: ClassVar[Literal['x']] = 'x'
    ELEMENTS_IN_SEQUENCE_COUNT: ClassVar[Literal[5]] = 8
    SEQUENCE_OPERATIONS_COUNT: ClassVar[Literal[2]] = 2
    
    def __init__(self):
        self.wins_count = 0

    def __generate_new_pattern(self):
        number = str(random.randint(2, 10))
        includes_var = random.randint(0, 10) > 5

        if includes_var:
            number = f'{number}*x'

        operation = random.choice(self.OPERATIONS_LIST)
        return f'{operation}{number}'

    def __generate_sequence_function(self) -> Callable[[SupportsInt], SupportsInt]:
        number = str(random.randint(0, 10))
        sequence_str = f'{number}'

        for _ in range(self.SEQUENCE_OPERATIONS_COUNT):
            new_pattern = self.__generate_new_pattern()
            sequence_str = ''.join((sequence_str, new_pattern))

        if self.VARIABLE_CHAR in sequence_str:
            return lambda x: eval(sequence_str), sequence_str
        return self.__generate_sequence_function()

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

    def __check_win(self):
        if self.wins_count == RIGHT_ANSWERS_TO_WIN_COUNT:
            raise StopGameException('Поздравляем! Вы отгадали 3 правильные последовательности!')

    def update(self):
        sequence_str, sequence, right_answer = self.__get_sequence_data()

        self.__ask_choice(right_answer, sequence, sequence_str)
        self.__check_win()

    def __get_sequence_data(self) -> tuple[str, Callable[[SupportsInt], SupportsInt], str]:
        ''' Создать новую последовательность и получить её функцию для вывода ответа и праивльный ответ '''
        sequence_function, sequence_str = self.__generate_sequence_function()
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
