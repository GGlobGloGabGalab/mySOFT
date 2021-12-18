from Qt5.QtWidgets import QWidget, QApplication

from MainLayout import 
class Mywindow(QWidget): #Создаем класс окна
    def __init__(self):
        super().__init__()
        self.mainLayout = mainLayout().
        self.setLayout(self.mainLayout)
        self.resize(400, 400) #Размеры окна
        self.show() #Показ окна