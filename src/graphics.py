import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

class Graph():
    """
    Класс для построения графиков с различными методами отображения.

    Attributes:
        x_points (np.array): Массив точек по оси X.
        y_points (np.array): Массив точек по оси Y.
        method (int): Метод отображения графика (1 - точки, 2 - кусочно-линейный, 3 - сглаженный и т.д.).
        x_label (str): Подпись для оси X.
        y_label (str): Подпись для оси Y.
        plot_label (str): Метка для легенды.
        plot_title (str): Заголовок графика.
        lim_x_left (float, optional): Левая граница по оси X.
        lim_x_right (float, optional): Правая граница по оси X.
        lim_y_top (float, optional): Верхняя граница по оси Y.
        lim_y_bottom (float, optional): Нижняя граница по оси Y.
        xerr (float, optional): Погрешность по оси X.
        yerr (float, optional): Погрешность по оси Y.
    """
    def __init__(self, x_points, y_points, method, x_label, y_label, 
                plot_label, plot_title, lim_x_left, lim_x_right, 
                lim_y_top, lim_y_bottom, xerr, yerr):
        
        self.y_points = y_points
        self.x_points = x_points
        self.method = method
        self.x_label = x_label
        self.y_label = y_label
        self.plot_label = plot_label
        self.plot_title = plot_title
        self.lim_x_left = lim_x_left
        self.lim_x_right = lim_x_right
        self.lim_y_top = lim_y_top
        self.lim_y_bottom = lim_y_bottom
        self.xerr = xerr
        self.yerr = yerr
        self.k = None  # Наклон для линейной аппроксимации y = kx
        self.b = None  # Смещение для линейной аппроксимации y = kx + b

    def show_points(self):
        """Отображает график в виде точек."""
        plt.scatter(self.x_points, self.y_points, label = self.plot_label)

    def show_piecewise_linear(self):
        """Отображает график как кусочно-линейный."""
        plt.plot(self.x_points, self.y_points, label = self.plot_label)

    def show_smooth(self):
        """Отображает сглаженный график с использованием сплайнов."""
        sorted_indices = np.argsort(self.x_points)
        x_sorted = self.x_points[sorted_indices]
        y_sorted = self.y_points[sorted_indices]
        x_new = np.linspace(x_sorted.min(), x_sorted.max(), 500)
        spl = make_interp_spline(x_sorted, y_sorted, k=3)
        y_smooth = spl(x_new)
        plt.plot(x_new, y_smooth, label = self.plot_label)

    def show_linear_y_kx(self):
        """Отображает линейную аппроксимацию y = kx."""
        self.k, _ = np.polyfit(self.x_points, self.y_points, 1)
        y_approx = self.k * self.x_points
        plt.plot(self.x_points, y_approx, label = self.plot_label)

    def show_linear_y_kx_plus_b(self):
        """Отображает линейную аппроксимацию y = kx + b."""
        self.k, self.b = np.polyfit(self.x_points, self.y_points, 1)
        y_approx = self.k * self.x_points + self.b
        plt.plot(self.x_points, y_approx, label = self.plot_label)

    def build_graph(self):
        """Строит график с учетом выбранного метода отображения."""
        plt.figure(figsize=(8, 6))
        
        # Отображение исходных точек с погрешностью, если указана
        plt.errorbar(self.x_points, self.y_points, xerr = self.xerr, yerr = self.yerr, fmt='o')

        # Выбор метода отображения
        if self.method == 1:
            self.show_points()
        elif self.method == 2:
            self.show_piecewise_linear()
        elif self.method == 3:
            self.show_smooth()
        elif self.method == 4:
            self.show_linear_y_kx()
        elif self.method == 5:
            self.show_linear_y_kx_plus_b()

        # Установка границ графика
        if self.lim_x_left == "":
            self.lim_x_left =  self.x_points.min()
        if self.lim_x_right == "":
            self.lim_x_right = self.x_points.max()
        if self.lim_y_bottom == "":
            self.lim_y_bottom = self.y_points.min()
        if self.lim_y_top == "":
            self.lim_y_top = self.y_points.max()

        plt.xlim(self.lim_x_left, self.lim_x_right)
        plt.ylim(self.lim_y_bottom, self.lim_y_top)

        # Настройка подписей
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.plot_title)
        if self.plot_label != "":
            plt.legend()
        plt.grid(True)

        # Отображение графика
        plt.show()