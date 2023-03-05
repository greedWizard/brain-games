from dataclasses import dataclass

from games.constants import RIGHT_ANSWERS_TO_WIN_COUNT
from games.exceptions import StopGameException


@dataclass
class BaseGame:
    is_running: bool = True
    wins_count: int = 0

    def get_win_message(self):
        ''' Функция должна возвращать сообщение о победе '''
        raise NotImplementedError()

    def _check_win(self):
        if self.wins_count == RIGHT_ANSWERS_TO_WIN_COUNT:
            raise StopGameException(self.get_win_message())

    def start(self):
        raise NotImplementedError()

    def update(self):
        raise NotImplementedError()

    @classmethod
    def init(cls):
        return cls()
