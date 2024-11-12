from PyQt5 import QtCore, QtGui, QtWidgets
from table_window import TableWindow
from table import TableText, TableLatex
from error_window import error_window

class TableGeneratorWindow(QtWidgets.QMainWindow):
    """
    Класс для настройки интерфейса окна генератора таблиц.
    """

    def __init__(self, variables_dict, constants_dict):
        super().__init__()
        self.variables_dict = variables_dict
        self.constants_dict = constants_dict
        self.setup_ui(self)

        # Создание экземпляра класса таблицы
        self.table_text = TableText("", self.variables_dict, self.constants_dict)
        self.table_latex = TableLatex("", self.variables_dict, self.constants_dict)

    def setup_ui(self, table_generator_window):
        """
        Настраивает интерфейс окна генератора таблиц.
        """
        table_generator_window.setObjectName("TableGeneratorWindow")
        table_generator_window.setFixedSize(294, 153)

        # Центральный виджет
        self.central_widget = QtWidgets.QWidget(table_generator_window)
        self.central_widget.setObjectName("centralwidget")

        # Основная метка с инструкцией
        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setGeometry(QtCore.QRect(20, 0, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # Поле ввода для данных
        self.input_field = QtWidgets.QLineEdit(self.central_widget)
        self.input_field.setGeometry(QtCore.QRect(10, 40, 271, 31))
        self.input_field.setText("")
        self.input_field.setObjectName("inputField")

        # Кнопка для генерации кода LaTeX
        self.generate_latex_button = QtWidgets.QPushButton(self.central_widget)
        self.generate_latex_button.setGeometry(QtCore.QRect(10, 80, 131, 41))
        font.setPointSize(9)
        self.generate_latex_button.setFont(font)
        self.generate_latex_button.setObjectName("generateLatexButton")
        self.generate_latex_button.clicked.connect(self.open_generate_latex_window)

        # Кнопка для сохранения таблицы в файл
        self.open_table_button = QtWidgets.QPushButton(self.central_widget)
        self.open_table_button.setGeometry(QtCore.QRect(150, 80, 131, 41))
        self.open_table_button.setFont(font)
        self.open_table_button.setObjectName("openTableButton")
        self.open_table_button.clicked.connect(self.open_table_text_window)

        # Установка центрального виджета
        table_generator_window.setCentralWidget(self.central_widget)

        # Строка состояния
        self.status_bar = QtWidgets.QStatusBar(table_generator_window)
        self.status_bar.setObjectName("statusbar")
        table_generator_window.setStatusBar(self.status_bar)

        self.retranslate_ui(table_generator_window)
        QtCore.QMetaObject.connectSlotsByName(table_generator_window)

    def retranslate_ui(self, table_generator_window):
        """
        Переводит и задает текст для виджетов интерфейса.
        """
        _translate = QtCore.QCoreApplication.translate
        table_generator_window.setWindowTitle(_translate("TableGeneratorWindow", "Генератор таблиц"))
        self.label.setText(_translate("TableGeneratorWindow", "Сгенерировать таблицу"))
        self.generate_latex_button.setText(_translate("TableGeneratorWindow", "Код LaTeX"))
        self.open_table_button.setText(_translate("TableGeneratorWindow", "Открыть таблицу"))

    def open_generate_latex_window(self):
        """
        Открывает окно кода таблицы для LaTeX.
        """
        self.table_latex.expression = self.input_field.text()
        if self.table_latex.table_print():
            self.table_latex_window = TableWindow(self.table_latex.output)
            self.table_latex_window.show()
        else:
            error_window()

    def open_table_text_window(self):
        """
        Открывает окно таблицы.
        """
        self.table_text.expression = self.input_field.text()
        if self.table_text.table_print():
            self.table_text_window = TableWindow(self.table_text.output)
            self.table_text_window.show()
        else:
            error_window()