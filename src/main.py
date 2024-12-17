import sys
from PyQt5 import QtWidgets
from choose_task_window import ChooseTaskWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    # Создание главного окна
    main_window = QtWidgets.QMainWindow()
    
    # Создание и настройка окна выбора задачи
    ui = ChooseTaskWindow()
    ui.setup_ui(main_window)
    
    # Отображение главного окна
    main_window.show()
    
    # Запуск приложения
    sys.exit(app.exec_())