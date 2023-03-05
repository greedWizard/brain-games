import sys
from typing import ClassVar

from simple_term_menu import TerminalMenu
from games.calculator_game import CalculatorGame

from games.common import BaseGame
from games.constants import (
    CALCULATOR_GAME_NAME,
    GCD_GAME_NAME,
    NO_CHOICE,
    ODD_EVEN_GAME_NAME,
    PRIME_GAME_NAME,
    SEQUENCE_GAME_NAME,
    YES_CHOICE,
)
from games.exceptions import StopGameException
from games.gcd import GCDGame
from games.odd_even import OddEvenGame
from games.prime import PrimeGame
from games.sequence import SequenceGame


class GameManager:
    GAMES_CHOICES: ClassVar[list[str]] = (
        SEQUENCE_GAME_NAME,
        CALCULATOR_GAME_NAME,
        ODD_EVEN_GAME_NAME,
        GCD_GAME_NAME,
        PRIME_GAME_NAME,
    )
    GAMES_CHOICES_MAP: ClassVar[dict] = {
        SEQUENCE_GAME_NAME: SequenceGame,
        CALCULATOR_GAME_NAME: CalculatorGame,
        ODD_EVEN_GAME_NAME: OddEvenGame,
        GCD_GAME_NAME: GCDGame,
        PRIME_GAME_NAME: PrimeGame,
    }

    current_GAME_NAME: BaseGame = None

    def change_GAME_NAME(self, index: int) -> BaseGame:
        assert index < len(self.GAMES_CHOICES), 'Данная игра не найдена в списке'

        game_key = self.GAMES_CHOICES[index]
        self.current_GAME_NAME = self.GAMES_CHOICES_MAP[game_key].init()

    def start(self):
        print('Выберите игру:')
        menu = TerminalMenu(self.GAMES_CHOICES)
        game_index = menu.show()
        self.change_GAME_NAME(game_index)
        self.run()

    def ask_restart(self):
        choice = input(f'Начать новую игру? {YES_CHOICE}/{NO_CHOICE}: ')

        if choice == YES_CHOICE:
            self.start()
        else:
            sys.exit()

    def run(self):
        assert self.current_GAME_NAME, 'Ни одна игра не запущена, пожалуйста выберите игру'
        self.current_GAME_NAME.start()

        while True:
            try:
                self.current_GAME_NAME.update()
            except StopGameException as error:
                print(str(error))
                self.ask_restart()
