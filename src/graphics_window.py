from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QComboBox, QPushButton, QSpinBox, QDoubleSpinBox
)
from graphics import Graph
from error_window import error_window

class GraphInputApp(QtWidgets.QMainWindow):
    """
    Класс для создания приложения, позволяющего вводить параметры для построения графика.

    Attributes:
        variables_dict (dict): Словарь с переменными для графиков.
    """
    def __init__(self, variables_dict):
        super().__init__()
        self.variables_dict = variables_dict
        self.setup_ui()
        

    def setup_ui(self):
        """
        Настройка пользовательского интерфейса.
        """
        self.setWindowTitle("Ввод параметров графика")
        self.setGeometry(100, 100, 400, 600)

        # Основной виджет и макет
        widget = QWidget()
        layout = QVBoxLayout()

        # Поля для ввода параметров
        self.fields = {
            "Ось X": QLineEdit(),
            "Ось Y": QLineEdit(),
            "Подпись к оси X": QLineEdit(),
            "Подпись к оси Y": QLineEdit(),
            "Подпись к графику": QLineEdit(),
            "Название графика": QLineEdit(),
            "Левая граница": QLineEdit(),
            "Правая граница": QLineEdit(),
            "Верхняя граница": QLineEdit(),
            "Нижняя граница": QLineEdit(),
            "Погрешность X": QLineEdit(),
            "Погрешность Y": QLineEdit(),
        }

        # Настройка полей
        for label, field in self.fields.items():
            layout.addWidget(QLabel(label))
            if isinstance(field, QDoubleSpinBox):
                field.setRange(-1e6, 1e6)
                field.setDecimals(2)
                field.setValue(0)
            layout.addWidget(field)

        # Поле для выбора метода отображения
        self.method_combo = QComboBox()
        self.method_combo.addItems([
            "1 - Точки", "2 - Кусочно-Линейная", "3 - Гладкая", "4 - Линейная y = kx", "5 - Линейная y = kx + b"
        ])
        layout.addWidget(QLabel("method"))
        layout.addWidget(self.method_combo)

        # Кнопка для построения графика
        self.plot_button = QPushButton("Build Graph")
        self.plot_button.clicked.connect(self.plot_builder)
        layout.addWidget(self.plot_button)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def plot_builder(self):
        """
        Обрабатывает вводимые данные и строит график.
        """

        x_points = self.fields["Ось X"].text().replace(" ", '')
        y_points = self.fields["Ось Y"].text().replace(" ", '')

        x_label = self.fields["Подпись к оси X"].text().replace(" ", '')
        y_label = self.fields["Подпись к оси Y"].text().replace(" ", '')

        plot_label = self.fields["Подпись к графику"].text().replace(" ", '')
        plot_title = self.fields["Название графика"].text().replace(" ", '')
        
        lim_x_left_text = self.fields["Левая граница"].text().replace(" ", '')
        lim_x_left = int(lim_x_left_text) if lim_x_left_text else None

        lim_x_right_text = self.fields["Правая граница"].text().replace(" ", '')
        lim_x_right = int(lim_x_right_text) if lim_x_right_text else None

        lim_y_top_text = self.fields["Верхняя граница"].text().replace(" ", '')
        lim_y_top = int(lim_y_top_text) if lim_y_top_text else None

        lim_y_bottom_text = self.fields["Нижняя граница"].text().replace(" ", '')
        lim_y_bottom = int(lim_y_bottom_text) if lim_y_bottom_text else None

        xerr_text = self.fields["Погрешность X"].text().replace(" ", '').replace(',', '.')
        if xerr_text:
            if any(char not in '1234567890.' for char in xerr_text):
                xerr = float(self.variables_dict.data_dict.get[xerr_text]) 
            else:
                xerr = float(xerr_text) 
        else:
            xerr = 0.0 

        yerr_text = self.fields["Погрешность Y"].text().replace(" ", '').replace(',', '.')
        if yerr_text:
            if any(char not in '1234567890.' for char in yerr_text):
                yerr = float(self.variables_dict.data_dict.get[yerr_text])
            else:
                yerr = float(yerr_text) 
        else:
            yerr = 0.0

        method = int(self.method_combo.currentText()[0])
        
        # Проверка введенных параметров
        if x_points not in self.variables_dict.data_dict:
            error_window()
            return
        else:
            x_points = self.variables_dict.data_dict[x_points]
        
        if y_points not in self.variables_dict.data_dict:
            error_window()
            return
        else:
            y_points = self.variables_dict.data_dict[y_points]

        # Построение графика
        graph = Graph(
            y_points=y_points,
            x_points=x_points,
            method=method,
            x_label=x_label,
            y_label=y_label,
            plot_label=plot_label,
            plot_title=plot_title,
            lim_x_left=lim_x_left,
            lim_x_right=lim_x_right,
            lim_y_top=lim_y_top,
            lim_y_bottom=lim_y_bottom,
            xerr=xerr,
            yerr=yerr
        )
        graph.build_graph()