from dataclasses import dataclass


@dataclass
class BaseGame:
    is_running: bool = True
    
    def start(self):
        raise NotImplementedError()

    def update(self):
        raise NotImplementedError()
    
    @classmethod
    def init(cls):
        return cls()
