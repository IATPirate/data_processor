from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from load_data_window import LoadDataWindow
from table_generator_window import TableGeneratorWindow
from formula_window import FormulaWindow
from graphics_window import GraphInputApp
from data import DataConstants, DataVariables
from formula import Formula
from error_window import error_window

class ChooseTaskWindow(QtWidgets.QMainWindow):
    """
    Класс, отвечающий за интерфейс окна выбора задачи.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui(self)

        # Создание словарей
        self.variables_dict = DataVariables("", [])
        self.constants_dict = DataConstants("", [])

        # Формула
        self.formula_expression = Formula('', '', self.variables_dict, self.constants_dict)

        # Путь к файлу
        self.path = ""

    def setup_ui(self, choose_task_window):
        """
        Настраивает интерфейс окна выбора задачи.
        """
        choose_task_window.setObjectName("ChooseTaskWindow")
        choose_task_window.resize(1002, 650)

        # Центральный виджет
        self.central_widget = QtWidgets.QWidget(choose_task_window)
        self.central_widget.setEnabled(True)
        self.central_widget.setObjectName("central_widget")

        # Кнопка "Загрузить данные"
        self.button_load_data = QtWidgets.QPushButton(self.central_widget)
        self.button_load_data.setGeometry(QtCore.QRect(90, 100, 821, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_load_data.setFont(font)
        self.button_load_data.setObjectName("LoadDataButton")
        self.button_load_data.clicked.connect(self.open_load_data_window)

        # Кнопка "Рассчитать данные по формуле"
        self.button_formula = QtWidgets.QPushButton(self.central_widget)
        self.button_formula.setGeometry(QtCore.QRect(90, 210, 821, 91))
        self.button_formula.setFont(font)
        self.button_formula.setObjectName("FormulaButton")
        self.button_formula.clicked.connect(self.open_formula_window)

        # Кнопка "Работа с графиками"
        self.button_graphics = QtWidgets.QPushButton(self.central_widget)
        self.button_graphics.setGeometry(QtCore.QRect(90, 320, 821, 91))
        self.button_graphics.setFont(font)
        self.button_graphics.setObjectName("GraphicsButton")
        self.button_graphics.clicked.connect(self.open_graphics_window)

        # Кнопка "Генерация таблиц"
        self.button_table_generator = QtWidgets.QPushButton(self.central_widget)
        self.button_table_generator.setGeometry(QtCore.QRect(90, 430, 821, 91))
        self.button_table_generator.setFont(font)
        self.button_table_generator.setObjectName("TableGeneratorButton")
        self.button_table_generator.clicked.connect(self.open_table_generator_window)

        # Установка центрального виджета
        choose_task_window.setCentralWidget(self.central_widget)

        # Метод для задания текста кнопок и окна
        self.retranslate_ui(choose_task_window)
        QtCore.QMetaObject.connectSlotsByName(choose_task_window)

    def retranslate_ui(self, choose_task_window):
        """
        Задает текст для виджетов в интерфейсе.
        """
        _translate = QtCore.QCoreApplication.translate
        choose_task_window.setWindowTitle(_translate("ChooseTaskWindow", "Выбор Задачи"))
        self.button_load_data.setText(_translate("ChooseTaskWindow", "Загрузить данные"))
        self.button_formula.setText(_translate("ChooseTaskWindow", "Рассчитать данные по формуле"))
        self.button_graphics.setText(_translate("ChooseTaskWindow", "Работа с графиками"))
        self.button_table_generator.setText(_translate("ChooseTaskWindow", "Генерация таблиц"))

    def open_load_data_window(self):
        """
        Открывает диалоговое окно для выбора файла и сохраняет путь к файлу и данные.
        """
        options = QFileDialog.Options()
        self.path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "All Files (*);;Text Files (*.txt)", options=options)
        check_dict = DataVariables(self.path, [])
        if self.path != "":
            number_of_columns, number_of_lines = check_dict.validate_data()
            if number_of_columns == 0:
                error_window()
            elif number_of_columns == 1:
                self.constants_dict = DataConstants(self.path, [])
                self.load_data_window = LoadDataWindow(number_of_lines, self.constants_dict)
                self.load_data_window.show()
            else:
                self.variables_dict = DataVariables(self.path, [])
                self.load_data_window = LoadDataWindow(number_of_columns, self.variables_dict)
                self.load_data_window.show()
        else:
            error_window()


    def open_formula_window(self):
        """
        Открывает окно для расчета данных по формуле.
        """
        self.formula_expression.variables_dict = self.variables_dict
        self.formula_expression.constants_dict = self.constants_dict
        self.formula_window = FormulaWindow(self.formula_expression)
        self.formula_window.show()

    def open_table_generator_window(self):
        """
        Открывает окно для генерации таблиц.
        """
        self.table_generator_window = TableGeneratorWindow(self.variables_dict, self.constants_dict)
        self.table_generator_window.show()

    def open_graphics_window(self):
        """
        Открывает окно для работы с графиками.
        """
        self.graphics_window = GraphInputApp(self.variables_dict)
        self.graphics_window.show()