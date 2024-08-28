# from PyQt6.QtWidgets import *
# app = QApplication([])
# window = QWidget()
# window.show()  
# # window1 = QWidget()
# # window1.show()  
# app.exec()
# # ör-2 >>>>>>>>>
# import sys
# from PyQt5.QtWidgets import *
# app = QApplication(sys.argv)
# window = QMainWindow()
# window.show()
# # Start the event loop.
# app.exec()
# # ör-3 >>>>>>>>>
# import sys
# # from PyQt5.QtWidgets import QApplication, QPushButton
# from PyQt5.QtWidgets import *
# app = QApplication(sys.argv)
# window = QPushButton("Tıkla")
# label=QLabel('merhaba')
# window.show()
# app.exec()

# import sys
# from PyQt6.QtWidgets import *
# app = QApplication(sys.argv)


# x = QWidget()
# x.setWindowTitle('Deneme')
# x.resize(300,50)
# x.setFixedSize(100, 100)
# x.show()

# window1 = QPushButton("Tıkla")
# window1.setWindowTitle('Deneme')
# window1.resize(300,50)
# window1.setFixedSize(100, 100)
# window1.show()  
# aa = QLabel("Merhaba")
# aa.show()

# app.exec()
# import sys
# from PyQt6 import QtWidgets
# app = QtWidgets.QApplication(sys.argv)
# button = QtWidgets.QPushButton("Merhaba")
# button.setFixedSize(100, 100)
# button.show()
# app.exec()
# # Buton ekleyelim
# from PyQt6.QtWidgets import *
# aa = QApplication([])

# ww = QWidget()

# icerik = QVBoxLayout()

# icerik.addWidget(QPushButton('Tıkla'))
# icerik.addWidget(QPushButton('Dene'))
# icerik.addWidget(QLabel('Bilgi'))

# ww.setLayout(icerik)

# ww.show()
# aa.exec()


# # Tıklama algılama
# from PyQt6.QtWidgets import *

# app = QApplication([])
# button = QPushButton('Click')

# def on_button_clicked():
#     alert = QMessageBox()
#     alert.setText('Tıkladın!')
#     alert.exec()

# button.clicked.connect(on_button_clicked)
# button.show()
# app.exec()