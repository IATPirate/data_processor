class Table():
    """
    Инициализация таблицы.

    Attributes:
        expression (str): Список выражений, для которых будет построена таблица.
        variables_dict (dict): Словарь переменных.
        constants_dict (dict): Словарь констант.
    """
    def __init__(self, expression, variables_dict, constants_dict):
        self.expression = expression
        self.variables_dict = variables_dict
        self.constants_dict = constants_dict
        self.output = ""

    def validate_variables(self):
        """
        Проверяет, что все переменные в выражении существуют в словарях переменных или констант.

        Returns:
            bool: True, если все переменные валидны, иначе False.
        """
        self.expression = list(filter(lambda x: x != "", self.expression.split()))
        if self.expression == []:
            return False
        for e in self.expression:
            if e not in self.variables_dict.data_dict and e not in self.constants_dict.data_dict:
                return False
        return True

class TableText(Table):
    def table_print(self):
        """
        Печатает таблицу в текстовом формате.

        Returns:
            bool: True, если таблица успешно сгенерирована, иначе False.
        """
        if self.validate_variables():
            for e in self.expression:
                self.output = self.output + e + " "
            self.output += "\n"
            table_len = 0
            for e in self.expression:
                if e in self.variables_dict.data_dict:
                    table_len = len(self.variables_dict.data_dict[e])
            for i in range(table_len):
                for e in self.expression:
                    if e in self.variables_dict.data_dict:
                        self.output = self.output + str(self.variables_dict.data_dict[e][i]) + " "
                    else:
                        self.output = self.output + str(self.constants_dict.data_dict[e]) + " "
                self.output += "\n"
            return True
        
        return False

class TableLatex(Table):
    def table_print(self):
        """
        Печатает таблицу в формате LaTeX.

        Returns:
            bool: True, если таблица успешно сгенерирована, иначе False.
        """
        if self.validate_variables():
            self.output = "\\begin{{table}}[H]\n\\begin{{center}}\n\\begin{{tabular}}{{|}}" + "c|" * len(self.expression) + "}}\n\\hline\n"
            for e in self.expression:
                self.output = self.output + "\\multicolumn{{1}}{{|c|}}{{" + e + "}} &"
            self.output = self.output[:-1] + "\\\\ \\hline\n"
            table_len = 0
            for e in self.expression:
                if e in self.variables_dict.data_dict:
                    table_len = len(self.variables_dict.data_dict[e])
            for i in range(table_len):
                for e in self.expression:
                    if e in self.variables_dict.data_dict:
                        self.output = self.output + "\\multicolumn{{1}}{{|c|}}{{" + str(self.variables_dict.data_dict[e][i]) + "}} &"
                    else:
                        self.output = self.output + "\\multicolumn{{1}}{{|c|}}{{" + str(self.variables_dict.data_dict[e]) + "}} &"
                self.output = self.output[:-1] + "\\\\ \\hline\n"
            self.output += "\\end{{tabular}}\n\\end{{center}}\n\\end{{table}}"
            return True
        
        return False