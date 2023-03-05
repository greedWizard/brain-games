import random
from typing import Callable, ClassVar, Literal, SupportsInt


class GenerateMathPatternMixin:
    OPERATIONS_LIST: ClassVar[list[str]] = [
        '+',
        '-',
        '*',
    ]
    VARIABLE_CHAR: ClassVar[Literal['x']] = 'x'
    SEQUENCE_OPERATIONS_COUNT: ClassVar[Literal[2]] = 2
    MIN_NUMBER_IN_EXPRESSION: ClassVar[int] = 0
    MAX_NUMBER_IN_EXPRESSION: ClassVar[int] = 10
    
    def _generate_math_expression(
        self,
        allow_parameter: bool = False,
        sequence_operations_count: int = 2,
    ) -> Callable[[SupportsInt], SupportsInt]:
        number = str(random.randint(self.MIN_NUMBER_IN_EXPRESSION, self.MAX_NUMBER_IN_EXPRESSION))
        sequence_str = f'{number}'

        for _ in range(sequence_operations_count):
            includes_var = random.randint(0, 10) > 5
            new_pattern = self.__generate_new_pattern(allow_parameter and includes_var)
            sequence_str = ''.join((sequence_str, new_pattern))

        if self.VARIABLE_CHAR not in sequence_str and includes_var:
            return self._generate_math_expression()
        elif allow_parameter:
            return lambda x: eval(sequence_str), sequence_str
        return lambda: eval(sequence_str), sequence_str
        
    
    def __generate_new_pattern(self, includes_var: bool = False):
        number = str(random.randint(self.MIN_NUMBER_IN_EXPRESSION, self.MAX_NUMBER_IN_EXPRESSION))

        if includes_var:
            number = f'{number}*x'

        operation = random.choice(self.OPERATIONS_LIST)
        return f'{operation}{number}'
