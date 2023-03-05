from typing import ClassVar

from simple_term_menu import TerminalMenu

from games.common import BaseGame
from games.constants import NO_CHOICE, YES_CHOICE
from games.exceptions import StopGameException
from games.sequence import SequenceGame


class GameManager:
    SEQUENCE_GAME: ClassVar[str] = 'sequence'
    CALCULATOR_GAME: ClassVar[str] = 'calculator'
    GAMES_CHOICES: ClassVar[list[str]] = (SEQUENCE_GAME, CALCULATOR_GAME)
    GAMES_CHOICES_MAP: ClassVar[dict] = {
        SEQUENCE_GAME: SequenceGame,
        CALCULATOR_GAME: None,
    }
    
    current_game: BaseGame = None
    
    def change_game(self, index: int) -> BaseGame:
        assert index < len(self.GAMES_CHOICES), 'Данная игра не найдена в списке'

        game_key = self.GAMES_CHOICES[index]
        self.current_game = self.GAMES_CHOICES_MAP[game_key].init()

    def start(self):
        print('Выберите игру:')
        menu = TerminalMenu(self.GAMES_CHOICES)
        game_index = menu.show()
        self.change_game(game_index)
        self.run()

    def ask_restart(self):
        choice = input(f'Начать новую игру? {YES_CHOICE}/{NO_CHOICE}')
        
        if choice == YES_CHOICE:
            self.start()

    def run(self):
        assert self.current_game, 'Ни одна игра не запущена, пожалуйста выберите игру'
        self.current_game.start()

        while True:
            try:
                self.current_game.update()
            except StopGameException as error:
                print(str(error))
                self.ask_restart()
