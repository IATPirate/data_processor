from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QLineEdit, QPushButton, QLabel
from error_window import error_window

class LoadDataWindow(QtWidgets.QMainWindow):
    """
    Класс, отвечающий за интерфейс окна загрузки данных.
    
    Attributes:
        num_edits (int): Количество полей ввода.
        data_dict (DataVariables): Словарь для хранения данных переменных.
    """
    def __init__(self, num_edits, data_dict):
        super().__init__()
        
        self.data_dict = data_dict
        self.num_edits = num_edits
        self.line_edits = []
        self.setup_ui()
    
    def setup_ui(self):
        """
        Настраивает пользовательский интерфейс окна загрузки данных.
        """
        self.central_widget = QtWidgets.QWidget(self)
        self.layout = QVBoxLayout(self.central_widget)
        
        # Кнопка загрузить данные
        self.get_button = QPushButton("Загрузить данные", self)
        self.get_button.clicked.connect(self.get_data)
        self.layout.addWidget(self.get_button)
        
        # Добавление QLabel и QLineEdit в layout и сохранение ссылок на QLineEdit
        for i in range(self.num_edits):
            self.label = QLabel(f"Поле переменных {i+1}", self)
            self.layout.addWidget(self.label) 

            self.line_edit = QLineEdit(self)
            self.line_edits.append(self.line_edit) 
            self.layout.addWidget(self.line_edit) 
        
        self.setCentralWidget(self.central_widget) 
        self.setWindowTitle('Введите переменные')

    def get_data(self):
        """
        Получает данные из полей ввода, проверяет их корректность и загружает.
        
        Если данные некорректны, выводит окно с сообщением об ошибке.
        """
        self.data_dict.format = [line_edit.text() for line_edit in self.line_edits]

        if self.data_dict.validate_variables():
            self.data_dict.load_data()
            self.close()
        else:
            error_window()