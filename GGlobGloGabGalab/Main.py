from PyQt5.QtWidgets import QApplication 

from MainWindow import MyWindow

if __name__ == '__main__':
    app = QApplication([]) #Создаем обЪект приложения
    window = MyWindow() #Создание объекта программы
    app.exec_() #вывод окна