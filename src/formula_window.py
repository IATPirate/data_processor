from PyQt5 import QtCore, QtGui, QtWidgets
from formula import Formula

class FormulaWindow(QtWidgets.QMainWindow):
    """
    Класс, который создает и настраивает окно ввода формулы приложения.
    
    Attributes:
        formula_expression (Formula): Экземпляр класса Formula для выполнения вычислений.
    """

    def __init__(self, formula_expression):
        super().__init__()
        self.formula_expression = formula_expression
        self.setup_ui(self)

    def setup_ui(self, formula_window):
        """
        Настраивает интерфейс окна ввода формулы приложения.
        """
        formula_window.setObjectName("FormulaWindow")
        formula_window.setFixedSize(456, 160)
        
        # Центральный виджет
        self.central_widget = QtWidgets.QWidget(formula_window)
        self.central_widget.setObjectName("centralwidget")

        # Поле ввода результата
        self.result_input = QtWidgets.QLineEdit(self.central_widget)
        self.result_input.setGeometry(QtCore.QRect(10, 50, 41, 41))
        self.result_input.setObjectName("resultInput")

        # Метка для знака "="
        self.equals_label = QtWidgets.QLabel(self.central_widget)
        self.equals_label.setGeometry(QtCore.QRect(60, 60, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.equals_label.setFont(font)
        self.equals_label.setObjectName("equalsLabel")

        # Поле ввода для формулы
        self.formula_input = QtWidgets.QLineEdit(self.central_widget)
        self.formula_input.setGeometry(QtCore.QRect(80, 50, 361, 41))
        self.formula_input.setObjectName("formulaInput")

        # Метка с инструкцией
        self.instruction_label = QtWidgets.QLabel(self.central_widget)
        self.instruction_label.setGeometry(QtCore.QRect(30, 10, 301, 31))
        font.setPointSize(12)
        self.instruction_label.setFont(font)
        self.instruction_label.setObjectName("instructionLabel")

        formula_window.setCentralWidget(self.central_widget)

        # Кнопка для рассчета формулы
        self.button_calculus = QtWidgets.QPushButton(self.central_widget)
        self.button_calculus.setGeometry(QtCore.QRect(330, 100, 111, 31))
        self.button_calculus.setObjectName("CalculusButton")
        self.button_calculus.clicked.connect(self.calculus)

        # Строка состояния
        self.status_bar = QtWidgets.QStatusBar(formula_window)
        self.status_bar.setObjectName("statusbar")
        formula_window.setStatusBar(self.status_bar)

        self.retranslate_ui(formula_window)
        QtCore.QMetaObject.connectSlotsByName(formula_window)

    def retranslate_ui(self, formula_window):
        """
        Переводит и задает текст для виджетов в интерфейсе.
        """
        _translate = QtCore.QCoreApplication.translate
        formula_window.setWindowTitle(_translate("FormulaWindow", "Окно ввода формулы"))
        self.instruction_label.setText(_translate("FormulaWindow", "Запишите формулу в формате np"))
        self.equals_label.setText(_translate("FormulaWindow", "="))
        self.button_calculus.setText(_translate("FormulaWindow", "Рассчитать"))

    def calculus(self):
        """
        Выполняет вычисление выражения, введенного пользователем.

        Устанавливает выражение и переменную для результата в формуле и вызывает функцию расчета.
        """
        self.formula_expression.expression = self.formula_input.text()
        self.formula_expression.variable = self.result_input.text()
        self.formula_expression.calculus()