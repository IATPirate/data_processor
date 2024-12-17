from PyQt5.QtWidgets import QMessageBox

def error_window():
    """
    Отображает окно предупреждения с сообщением об ошибке ввода.

    Выводит окно с заголовком "Ошибка" и сообщением "Неверный формат ввода".
    """
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.setWindowTitle("Ошибка")
    msg_box.setText("Неверный формат ввода")
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec_()