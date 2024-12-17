from PyQt5 import QtCore, QtGui, QtWidgets

class TableWindow(QtWidgets.QMainWindow):
    """
    Класс для управление окном отображения таблицы. 
    """

    def __init__(self, output):
        super().__init__()
        self.output = output
        self.setup_ui(self)

    def setup_ui(self, table_window):
        """
        Настраивает интерфейс окна таблиц.
        """
        table_window.setObjectName("TableWindow")
        table_window.setFixedSize(800, 603)
        
        # Центральный виджет
        self.centralwidget = QtWidgets.QWidget(table_window)
        self.centralwidget.setObjectName("centralwidget")
        
        # Поле для ввода текста
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 50, 801, 531))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setText(self.output)
        
        # Кнопка для сохранения текста
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.save_text_to_file)
        
        # Установка центрального виджета и строки состояния
        table_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(table_window)
        self.statusbar.setObjectName("statusbar")
        table_window.setStatusBar(self.statusbar)

        # Устанавливаем тексты для интерфейса
        self.retranslateUi(table_window)
        QtCore.QMetaObject.connectSlotsByName(table_window)

    def retranslateUi(self, MainWindow):
        """
        Переводит и задает текст для виджетов интерфейса.
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("TableWindow", "Окно Таблицы"))
        self.pushButton.setText(_translate("TableWindow", "Сохранить текст в файл"))

    def save_text_to_file(self):
        """
        Сохраняет содержимое текстового поля в файл.

        Открывает диалоговое окно для выбора файла, затем сохраняет текст из поля
        QTextEdit в выбранный файл. Поддерживаются текстовые файлы (.txt).
        """
        text = self.textEdit.toPlainText()
        
        options = QtWidgets.QFileDialog.Options()
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить текст", "", "Text Files (*.txt);;All Files (*)", options=options)
        
        if file_name:
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(text)