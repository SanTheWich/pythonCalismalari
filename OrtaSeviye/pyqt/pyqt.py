from PyQt6.QtWidgets import *
app = QApplication([])
window = QWidget()
window.show()  
# window1 = QWidget()
# window1.show()  
app.exec()
# ör-2 >>>>>>>>>
import sys
from PyQt5.QtWidgets import *
app = QApplication(sys.argv)
window = QMainWindow()
window.show()
# Start the event loop.
app.exec()
# ör-3 >>>>>>>>>
import sys
# from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtWidgets import *
app = QApplication(sys.argv)
window = QPushButton("Tıkla")
label=QLabel('merhaba')
window.show()
app.exec()