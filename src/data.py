import numpy as np

class DataLoader:
    """
    Класс для загрузки и валидации данных из файла.
    
    Attributes:
        path (str): Путь к файлу данных.
        format (list): Формат данных, представляющий список имен переменных или констант.
        data_dict (dict): Словарь для хранения загруженных данных.
    """
    def __init__(self, path, format):
        self.path = path
        self.format = format
        self.data_dict = {}

    def validate_data(self):
        """
        Проверяет данные на корректность. Проверка формата и согласованности строк и столбцов.
        
        Returns:
            tuple: Количество столбцов и строк в данных, если данные корректны; (0, 0) в противном случае.
        """
        with open(self.path, 'r') as file:
            number_of_columns = -1
            number_of_lines = 0

            for line in file:
                if any(char not in '1234567890., \n' for char in line):
                    return 0, 0
                
                current_row = list(filter(lambda x: x != "", line.replace(',', '.').split()))

                if number_of_columns != -1 and len(current_row) != number_of_columns:
                    return 0, 0
                number_of_columns = len(current_row)
                number_of_lines += 1
        
        return number_of_columns, number_of_lines

    def validate_variables(self):
        """
        Проверяет корректность имен переменных в формате данных.
        
        Returns:
            bool: True, если формат корректен, False в противном случае.
        """
        self.format = [f.replace(' ', '') for f in self.format]
        
        if not all(f.isidentifier() for f in self.format) or not all(len(f) > 0 for f in self.format):
            return False

        if len(set(self.format)) != len(self.format):
            return False

        return True

class DataVariables(DataLoader):
    """
    Класс для загрузки переменных из файла и их хранения в виде словаря.
    """
    def load_data(self):
        """
        Загружает данные переменных из файла и сохраняет их в словаре.
        """
        with open(self.path, 'r') as file:
            for line in file:
                row = list(filter(lambda x: x != "", line.replace(',', '.').split()))
                
                for i in range(len(row)):
                    if i >= len(self.format):
                        continue  # если данных больше, чем имен переменных в формате

                    key = self.format[i]
                    if key not in self.data_dict:
                        self.data_dict[key] = []
                    
                    self.data_dict[key] = np.append(self.data_dict[key], float(row[i]))

class DataConstants(DataLoader):
    """
    Класс для загрузки констант из файла и их хранения в виде словаря.
    """
    def load_data(self):
        """
        Загружает данные констант из файла и сохраняет их в словаре.
        """
        with open(self.path, 'r') as file:
            for i, line in enumerate(file):
                line = line.replace(',', '.').strip()

                self.data_dict[self.format[i]] = float(line)