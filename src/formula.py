import numpy as np
from error_window import error_window

class Formula():
    """
    Класс для выполнения вычислений на основе выражений и данных переменных и констант.

    Attributes:
        expression (str): Выражение для вычислений.
        variable (str): Имя переменной, в которую будут сохранены результаты.
        variables_dict (DataVariables): Словарь переменных.
        constants_dict (DataConstants): Словарь констант.
        data_dict (dict): Объединенный словарь данных для вычислений.
    """
    def __init__(self, expression, variable, variables_dict, constants_dict):
        self.variables_dict = variables_dict
        self.constants_dict = constants_dict
        self.expression = expression
        self.variable = variable
        self.data_dict = {}

    def validate_variable(self):
        """
        Проверяет, можно ли использовать переменную для сохранения результата.

        Returns:
            bool: True, если переменная не используется в data_dict; False иначе.
        """
        self.expression.replace(' ', '')
        self.data_dict = {**self.variables_dict.data_dict, **self.constants_dict.data_dict}
        for key in self.data_dict:
            if key == self.variable:
                return False
        return True

    def calculus(self):
        """
        Выполняет вычисление выражения и сохраняет результат в переменной.

        Если переменная допустима и вычисление успешно, результат сохраняется в variables_dict.
        Если переменная недопустима или вычисление вызывает ошибку, отображается окно с сообщением об ошибке.
        """
        if self.validate_variable():
            try:
                self.result = eval(self.expression, {"np": np}, self.data_dict)
                self.variables_dict.data_dict[self.variable] = self.result
            except:
                error_window()
        else:
            error_window()